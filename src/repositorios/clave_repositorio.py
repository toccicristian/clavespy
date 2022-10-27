import os
from os.path import isfile, normpath, expanduser
import repositorios.configuracion_repositorio as config
import herramientas.encriptacion

def existen_claves():
    try:
        with open(normpath(expanduser(
            config.obtiene_configuracion().clavebd)),'rb') as ar_r:
            if len(ar_r.read())>0: return True

    except FileNotFoundError:
        return False

    return False


def autenticar_clave(clave=''):
    if not existen_claves(): return False

    herramientas.encriptacion.desencriptar_ar(
        normpath(expanduser(config.obtiene_configuracion().clavebd)),
        herramientas.encriptacion.hashear(clave),
        normpath(expanduser(config.obtiene_configuracion().temp)))

    if not isfile(normpath(expanduser(
        config.obtiene_configuracion().temp))):
        return False

    try:
        with open(normpath(expanduser(
            config.obtiene_configuracion().temp)),'r') as ar_r:
            if ar_r.read() == herramientas.encriptacion.hashear(clave):
                os.remove(normpath(expanduser(
                    config.obtiene_configuracion().temp)))
                return True
    except UnicodeDecodeError:
        os.remove(normpath(expanduser(config.obtiene_configuracion().temp)))
        return False

    except FileNotFoundError:
        return False

    os.remove(normpath(expanduser(config.obtiene_configuracion().temp)))
    return False


def registrar_clave(clave=''):
    with open(normpath(expanduser(
        config.obtiene_configuracion().temp)),'w') as ar_w:
        ar_w.write(herramientas.encriptacion.hashear(clave))

    herramientas.encriptacion.encriptar_ar(
        normpath(expanduser(
            config.obtiene_configuracion().temp)),
        herramientas.encriptacion.hashear(clave),
                 normpath(expanduser(
                     config.obtiene_configuracion().clavebd)))
    os.remove(normpath((expanduser(
        config.obtiene_configuracion().temp))))

