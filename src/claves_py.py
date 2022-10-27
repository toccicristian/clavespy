#!/usr/bin/python3

import os
from os.path import isfile, normpath, expanduser
import sys
import shutil
import hashlib
import json


SYSBD='./sys.json'
CLAVEBD='./clave'
TEMP='./tmp'
SYSBACKUP='./sys.backup'
MASCARACODIGO='00000'
ANCHO_NOMBRE=25
ANCHO_DETALLE=40
DIVISOR_DE_LINEA='='

class Registro:
    def __init__(self,nombre='',cuit='',detalle='',clave=''):
        self._codigo=''
        self._nombre=nombre
        self._cuit=cuit
        self._detalle=detalle
        self._clave=clave
        self._borrado=False

    def get_nombre(self):
        return self._nombre

    def get_cuit(self):
        return self._cuit

    def get_detalle(self):
        return self._detalle

    def get_clave(self):
        return self._clave

    def get_codigo(self):
        return self._codigo

    def get_borrado(self):
        return self._borrado

    def set_codigo(self,codigo=''):
        self._codigo=codigo

    def set_borrado(self,borrado=True):
        self._borrado=borrado

    def to_str(self, ancho_nombre=25, ancho_detalle=40):
        return f'{self._codigo} {self._nombre.ljust(ancho_nombre)} {self._cuit} {self._detalle.ljust(ancho_detalle)} {self._clave}'


def es_numero(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def modulo(n):
    if n<0:
        return n*-1
    return n


def rota_b(val_b=0,veces=0,reverso=False, bits=256):
    if not reverso:
        r=val_b+veces
        if r > bits:
            r=r-bits
        return r
    r=val_b-veces
    if r < 0:
        r=bits+r
    return r


def hashear(cadena=str()):
    return hashlib.sha256(str(cadena).encode('utf-8')).hexdigest()


def encriptar_ar(url_in,clave,url_out):
    ba=bytearray()
    with open(url_in,'rb') as ar_r:
        ar=ar_r.read()
    pos_clave=0
    tam_total=os.path.getsize(url_in)
    bytes_leidos=0
    for byte in ar:
        ba.append(rota_b(val_b=byte,veces=ord(clave[pos_clave])))
        pos_clave+=1
        if not pos_clave < len(clave):
            pos_clave=0
        bytes_leidos+=1
        #print('\r['+str(round(bytes_leidos*100/tam_total))+'%] Bytes procesados '+str(bytes_leidos)+'/'+str(tam_total),end='',flush=True)
    #print('')
    with open(url_out,'wb') as ar_w:
        ar_w.write(ba)
    return None


def desencriptar_ar(url_in,clave,url_out):
    ba=bytearray()
    with open(url_in,'rb') as ar_r:
        ar=ar_r.read()
    pos_clave=0
    byte_ind=0
    tam_total=os.path.getsize(url_in)
    bytes_leidos=0
    for byte in ar:
        ba.append(rota_b(val_b=byte,veces=ord(clave[pos_clave]),reverso=True))
        pos_clave+=1
        if not pos_clave < len(clave):
            pos_clave=0
        bytes_leidos+=1
        #print('\r['+str(round(bytes_leidos*100/tam_total))+'%]Bytes procesados '+str(bytes_leidos)+'/'+str(tam_total),end='',flush=True)
    #print('')
    with open(url_out,'wb') as ar_w:
        ar_w.write(ba)
    return None


def existen_claves():
    try:
        with open(normpath(expanduser(CLAVEBD)),'rb') as ar_r:
            if len(ar_r.read())>0:
                return True
    except FileNotFoundError:
        return False

    return False


def autenticar_clave(clave=''):
    if not isfile(normpath(expanduser(CLAVEBD))):
        return False

    desencriptar_ar(normpath(expanduser(CLAVEBD)),hashear(clave),normpath(expanduser(TEMP)))
    if not isfile(normpath(expanduser(TEMP))):
        return False

    ar_r=open(normpath(expanduser(TEMP)),'r')
    try:
        if ar_r.read() == hashear(clave):
            ar_r.close()
            os.remove(normpath(expanduser(TEMP)))
            return True
    except UnicodeDecodeError:
        return False

    return False


def registrar_clave(clave=''):
    ar_w=open(normpath(expanduser(TEMP)),'w')
    ar_w.write(hashear(clave))
    ar_w.close()
    encriptar_ar(normpath(expanduser(TEMP)),hashear(clave),normpath(expanduser(CLAVEBD)))
    os.remove(normpath(expanduser(TEMP)))


def leer_bd(clave=''):
    registros=[]
    if not isfile(normpath(expanduser(SYSBD))):
        return registros
    desencriptar_ar(normpath(expanduser(SYSBD)),hashear(clave),normpath(expanduser(TEMP)))
    ar_r=open(normpath(expanduser(TEMP)),'r')
    regdict_list=json.load(ar_r)
    ar_r.close()
    os.remove(normpath(expanduser(TEMP)))
    for r in regdict_list:
        registro=Registro()
        registro.__dict__=r
        registros.append(registro)
    return registros


def guardar_bd(registros=[], clave=''):
    regdict_list=[]
    for r in registros:
        regdict_list.append(r.__dict__)
    ar_w=open(normpath(expanduser(TEMP)),'w')
    json.dump(regdict_list,ar_w)
    ar_w.close()
    encriptar_ar(normpath(expanduser(TEMP)),hashear(clave),normpath(expanduser(SYSBD)))
    os.remove(normpath(expanduser(TEMP)))


def agrega_registro(registro=Registro(),clave=''):
    registros=leer_bd(clave)
    try:
        registro.set_codigo(str(int(max([r.get_codigo() for r in registros]))+1).zfill(len(MASCARACODIGO)))
    except ValueError:
        registro.set_codigo(MASCARACODIGO)

    registros.append(registro)
    guardar_bd(registros,clave)


def borra_registro(codigo='', clave=''):
    reg=leer_bd(clave)
    reg[reg.index([r for r in reg if r.get_codigo() == str(codigo).zfill(len(MASCARACODIGO))][0])].set_borrado(borrado=True)
    guardar_bd(registros=reg, clave=clave)


def restaura_registro_borrado(codigo='', clave=''):
    reg=leer_bd(clave)
    reg[reg.index([r for r in reg if r.get_codigo() == str(codigo).zfill(len(MASCARACODIGO))][0])].set_borrado(borrado=False)
    guardar_bd(registros=reg, clave=clave)


def barre_registros_borrados(clave=''):
    reg=leer_bd(clave)
    res=[]
    [res.append(r) for r in reg if not r.get_borrado()]
    guardar_bd(registros=reg, clave=clave)


def imprime_titulo():
    print(f'{"CODIGO".ljust(len(MASCARACODIGO))} {"NOMBRE".ljust(ANCHO_NOMBRE)}{"CUIT".ljust(11)} {"DETALLE".ljust(ANCHO_DETALLE)} {"CLAVE"}')
    for _ in range(0,len(MASCARACODIGO)+ANCHO_NOMBRE+11+ANCHO_DETALLE+20):
        print(DIVISOR_DE_LINEA,end='')
    print('')


def imprime_registros(clave=''):
    listado=leer_bd(clave)
    for reg in listado:
        if not reg.get_borrado():
            print(f'{reg.to_str(ancho_nombre=ANCHO_NOMBRE, ancho_detalle=ANCHO_DETALLE)}')


def imprime_registros_borrados(clave=''):
    listado=leer_bd(clave)
    for reg in listado:
        if reg.get_borrado():
            print(f'{reg.to_str(ancho_nombre=ANCHO_NOMBRE, ancho_detalle=ANCHO_DETALLE)}')



for arg in sys.argv:
    if arg in ['-h','--help','--ayuda']:
        print('SINTAXIS :')
        print(f'\t{sys.argv[0]} -a \'nombre;cuit;detalle;clave\'\tAgrega registro.')
        print(f'\t{sys.argv[0]} -d CODIGO\tElimina registro correspondiente a dicho CODIGO.')
        print(f'\t{sys.argv[0]} -r CODIGO\tRestaura registro borrado correspondiente a dicho CODIGO.')
        print(f'\t{sys.argv[0]} --borrados\tImprime sólo registros que han sido borrados.')
        print(f'\t{sys.argv[0]}\tImprime los registros (excepto los borrados).')
        print(f'\t{sys.argv[0]} -p CLAVE\tSe salta el prompt que pide la clave y autentica CLAVE en lugar.')
        print(f'\t{sys.argv[0]} --barrer-borrados\tElimina de la base de datos los registros marcados como borrados.')
        sys.exit()

if not existen_claves():
    entrada=input('No hay claves registradas. Ingrese nueva clave y vuelva a iniciar:')
    if input(f'La clave ingresada fue : \"{entrada}\". Confirma? [s,n]').lower() == 's':
        registrar_clave(entrada)
    sys.exit()

hay_clave=False
for arg in sys.argv:
    if arg == '-p' and len(sys.argv)>sys.argv.index('-p')+1:
        clave=sys.argv[sys.argv.index('-p')+1]
        hay_clave=True

if not hay_clave:
    clave=input('Ingrese la clave de acceso :')

if not autenticar_clave(clave):
    print('La clave es incorrecta; saliendo...')
    sys.exit()

for arg in sys.argv:
    if arg == '-a' and len(sys.argv)>sys.argv.index('-a')+1 and len(sys.argv[sys.argv.index('-a')+1].split(';'))==4:
        r=sys.argv[sys.argv.index('-a')+1].split(';')
        reg=Registro(nombre=r[0],cuit=r[1],detalle=r[2],clave=r[3])
        agrega_registro(registro=reg, clave=clave)
        sys.exit()

    if arg == '-d' and len(sys.argv)>sys.argv.index('-d')+1 and es_numero(sys.argv[sys.argv.index('-d')+1]):
        borra_registro(codigo=sys.argv[sys.argv.index('-d')+1], clave=clave)
        sys.exit()

    if arg == '-r' and len(sys.argv)>sys.argv.index('-r')+1 and es_numero(sys.argv[sys.argv.index('-r')+1]):
        restaura_registro_borrado(codigo=sys.argv[sys.argv.index('-r')+1], clave=clave)
        sys.exit()

    if arg == '--borrados':
        imprime_titulo()
        imprime_registros_borrados(clave=clave)
        sys.exit()

    if arg == '--barrer-borrados':
        if isfile(normpath(expanduser(SYSBD))):
            if input('ESTA A PUNTO DE ELIMINAR TODOS LOS REGISTROS MARCADOS COMO BORRADOS! Proceder? [s,n]').lower() == 's':
                print(f'Resguardando {SYSBD}...')
                shutil.copy2(normpath(expanduser(SYSBD)),normpath(expanduser(SYSBACKUP)))
                barre_registros_borrados(clave=clave)
        sys.exit()

if len(sys.argv) == 1 or sys.argv[1]=='-p':
        imprime_titulo()
        imprime_registros(clave=clave)

