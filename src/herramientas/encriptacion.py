import hashlib
import herramientas.numeros
import os


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
        ba.append(herramientas.numeros.rota_b(val_b=byte,veces=ord(clave[pos_clave])))
        pos_clave+=1
        if not pos_clave < len(clave):
            pos_clave=0
        bytes_leidos+=1
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
        ba.append(herramientas.numeros.rota_b(val_b=byte,veces=ord(clave[pos_clave]),reverso=True))
        pos_clave+=1
        if not pos_clave < len(clave):
            pos_clave=0
        bytes_leidos+=1
    with open(url_out,'wb') as ar_w:
        ar_w.write(ba)
    return None


def desencriptar_ram(url_in,clave):
    ba=bytearray()
    with open(url_in,'rb') as ar_r:
        ar=ar_r.read()
    pos_clave=0
    byte_ind=0
    tam_total=os.path.getsize(url_in)
    bytes_leidos=0
    for byte in ar:
        ba.append(herramientas.numeros.rota_b(val_b=byte,veces=ord(clave[pos_clave]),reverso=True))
        pos_clave+=1
        if not pos_clave < len(clave):
            pos_clave=0
        bytes_leidos+=1
    return ba


