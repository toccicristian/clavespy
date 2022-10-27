from constantes.rutas import ARCHIVO_CONFIGURACION
from constantes.simbolos import ASIGNAR
import modelos.configuracion_modelo
from os.path import isfile, normpath, expanduser


def escribe_configuracion(config=modelos.configuracion_modelo.Configuracion()):
    with open(normpath(expanduser(ARCHIVO_CONFIGURACION)),'w') as ar_w:
        for a in [f'{atrib.upper()}{ASIGNAR}{config.__dict__["_"+atrib]}' for atrib  in dir(config) if not atrib.startswith('_')]:
            ar_w.write(f'{a}\n')


def busca_parametro(param=''):
    with open(normpath(expanduser(ARCHIVO_CONFIGURACION)),'r') as ar_r:
        for linea in ar_r.readlines():
            if linea.split(ASIGNAR)[0]==param and len(linea.split(ASIGNAR))>1:
                return linea.split(ASIGNAR)[1].rstrip('\n')
        return None


def obtiene_configuracion():
    config=modelos.configuracion_modelo.Configuracion()
    if not isfile(normpath(expanduser(ARCHIVO_CONFIGURACION))):
        escribe_configuracion(config)

    for a in [atrib for atrib in dir(config) if not atrib.startswith('_')]:
        if busca_parametro(a.upper()) is not None:
            config.__dict__[f'_{a}']=busca_parametro(a.upper())
    return config
