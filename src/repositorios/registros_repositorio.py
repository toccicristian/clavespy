from os.path import isfile, normpath, expanduser
import repositorios.configuracion_repositorio as conf
import herramientas.encriptacion as encript
import modelos.registro_modelo
import json
import os


def leer_bd(clave=''):
    registros=[]
    if not isfile(normpath(expanduser(conf.obtiene_configuracion().sysbd))):
        return registros
    encript.desencriptar_ar(normpath(expanduser(conf.obtiene_configuracion().sysbd)),
                    encript.hashear(clave),normpath(expanduser(conf.obtiene_configuracion().temp)))
    ar_r=open(normpath(expanduser(conf.obtiene_configuracion().temp)),'r', encoding='utf-8')
    regdict_list=json.load(ar_r)
    ar_r.close()
    os.remove(normpath(expanduser(conf.obtiene_configuracion().temp)))
    for r in regdict_list:
        registro=modelos.registro_modelo.Registro()
        registro.__dict__=r
        registros.append(registro)
    return registros


def guardar_bd(registros=[], clave=''):
    regdict_list=[]
    for r in registros:
        regdict_list.append(r.__dict__)
    ar_w=open(normpath(expanduser(conf.obtiene_configuracion().temp)),'w')
    json.dump(regdict_list,ar_w)
    ar_w.close()
    encript.encriptar_ar(normpath(expanduser(conf.obtiene_configuracion().temp)),
                 encript.hashear(clave),normpath(expanduser(conf.obtiene_configuracion().sysbd)))
    os.remove(normpath(expanduser(conf.obtiene_configuracion().temp)))


def agrega_registro(registro= modelos.registro_modelo.Registro(),clave=''):
    registros=leer_bd(clave)
    try:
        registro.codigo=str(int(max([r.codigo for r in registros]))+1).zfill(
            len(conf.obtiene_configuracion().mascara_codigo))
    except ValueError:
        registro.codigo=conf.obtiene_configuracion().mascara_codigo

    registros.append(registro)
    guardar_bd(registros,clave)


def borra_registro(codigo='', clave=''):
    reg=leer_bd(clave)
    reg[reg.index([r for r in reg if r.codigo == str(codigo).zfill(
        len(conf.obtiene_configuracion().mascara_codigo))][0])].borrado=True
    guardar_bd(registros=reg, clave=clave)


def restaura_registro_borrado(codigo='', clave=''):
    reg=leer_bd(clave)
    reg[reg.index([r for r in reg if r.codigo == str(codigo).zfill(
        len(conf.obtiene_configuracion().mascara_codigo))][0])].borrado=False
    guardar_bd(registros=reg, clave=clave)


def barre_registros_borrados(clave=''):
    cod=conf.obtiene_configuracion().mascara_codigo
    registros=leer_bd(clave)
    res=[]
    for r in [reg for reg in registros if not reg.borrado]:
        r.codigo=cod
        res.append(r)
        cod=str(int(cod)+1).zfill(len(cod))

    guardar_bd(registros=res, clave=clave)


def oblitera_registro(codigo='',clave=''):
    bd=leer_bd(clave)
    res=[]
    cod=conf.obtiene_configuracion().mascara_codigo
    for reg in [r for r in bd if r.codigo != codigo]:
        reg.codigo=cod
        res.append(reg)
        cod=str(int(cod)+1).zfill(len(cod))

    guardar_bd(registros=res, clave=clave)


def busca_registro_por_nombre(criterio='',clave='', borrados=False):
    bd=leer_bd(clave)
    res=[]
    [res.append(r) for r in bd if (criterio.upper() in r.nombre.upper() or all(item in r.nombre.upper().split(' ') for item in criterio.upper().split('+'))) and r.borrado == borrados]
    res.sort(key = lambda x : x.nombre, reverse=False)
    return res


def busca_registro_por_cuit(criterio='',clave='', borrados=False):
    bd=leer_bd(clave)
    res=[]
    [res.append(r) for r in bd if (criterio in r.cuit or all(item in r.cuit for item in criterio.split('+'))) and r.borrado is borrados]
    res.sort(key = lambda x : x.cuit, reverse=False)
    return res


def busca_registro_por_codigo(criterio='',clave='',borrados=False):
    bd=leer_bd(clave)
    res=[]
    for i in bd:
        if i.codigo == str(criterio).zfill(len(conf.busca_parametro("MASCARA_CODIGO"))):
            res.append(i)
    return res[0]


def intercambia_dos_registros(codigo1='',codigo2='',clave=''):
    bd=leer_bd(clave)

    registro1=modelos.registro_modelo.Registro(
        nombre=[r for r in bd if r.codigo == codigo1][0].nombre,
        cuit=[r for r in bd if r.codigo == codigo1][0].cuit,
        detalle=[r for r in bd if r.codigo == codigo1][0].detalle,
        clave=[r for r in bd if r.codigo == codigo1][0].clave)
    registro1.codigo=[r for r in bd if r.codigo == codigo1][0].codigo

    registro2=modelos.registro_modelo.Registro(
        nombre=[r for r in bd if r.codigo == codigo2][0].nombre,
        cuit=[r for r in bd if r.codigo == codigo2][0].cuit,
        detalle=[r for r in bd if r.codigo == codigo2][0].detalle,
        clave=[r for r in bd if r.codigo == codigo2][0].clave)
    registro2.codigo=[r for r in bd if r.codigo == codigo2][0].codigo

    tmp=registro1.codigo
    registro1.codigo=registro2.codigo
    registro2.codigo=tmp

    bd[bd.index([r for r in bd if r.codigo == codigo1][0])] = registro2
    bd[bd.index([r for r in bd if r.codigo == codigo2][0])] = registro1

    guardar_bd(bd,clave)
