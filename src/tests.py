#!/usr/bin/python3

import constantes.simbolos
import repositorios.configuracion_repositorio as conf
import repositorios.clave_repositorio
import repositorios.registros_repositorio
import modelos.registro_modelo
import os
import shutil
from os.path import isfile, normpath, expanduser
import vistas.v_principal
import vistas.v_login
import vistas.v_crearclave
import vistas.ventana_msg_ui as msg_w
import modelos.ventana_modelo as w
import tkinter as tk

clavedeprueba='clavedeprueba'
clavedeprueba2=f'{clavedeprueba}asdlkj'


def test_configuracion_repositorio_obtiene_configuracion():
    print('obtiene_configuracion')
    config=conf.obtiene_configuracion()
    for atr in [a for a in dir(config) if not a.startswith('_')]:
        print(f'  {atr.upper()}{constantes.simbolos.ASIGNAR}{config.__dict__["_"+atr]}')


def test_clave_repositorio_registrar_clave():
    if isfile(normpath(expanduser(conf.obtiene_configuracion().clavebd))):
        shutil.move(normpath(expanduser(
            conf.obtiene_configuracion().clavebd)),
                  normpath(expanduser(f'_testing_')))
    repositorios.clave_repositorio.registrar_clave(clavedeprueba)
    print(f'registrar_clave:                 \
        {isfile(normpath(expanduser(conf.obtiene_configuracion().clavebd)))}')
    os.remove(normpath(expanduser(conf.obtiene_configuracion().clavebd)))
    if isfile(normpath(expanduser(f'_testing_'))):
        shutil.move(normpath(expanduser(f'_testing_')),
                normpath(expanduser(conf.obtiene_configuracion().clavebd)))


def test_clave_repositorio_existen_claves():
    print(f'existen_claves:            \
              {repositorios.clave_repositorio.existen_claves()}')


def test_clave_repositorio_autenticar_clave():
    print('(Asumiendo registrar_clave: True)')
    if isfile(normpath(expanduser(conf.obtiene_configuracion().clavebd))):
        shutil.move(normpath(expanduser(
            conf.obtiene_configuracion().clavebd)),
                  normpath(expanduser(f'_testing_')))
    repositorios.clave_repositorio.registrar_clave(clavedeprueba)
    print(f'autenticar_clave (correcta):   \
          {repositorios.clave_repositorio.autenticar_clave(clavedeprueba)}')
    print(f'autenticar_clave (incorrecta): \
          {repositorios.clave_repositorio.autenticar_clave(clavedeprueba2)}')
    os.remove(normpath(expanduser(conf.obtiene_configuracion().clavebd)))
    if isfile(normpath(expanduser(f'_testing_'))):
        shutil.move(normpath(expanduser(f'_testing_')),
                normpath(expanduser(conf.obtiene_configuracion().clavebd)))


def test_registros_repositorio():
    print('registros_repositorio:')
    if isfile(normpath(expanduser(repositorios.configuracion_repositorio.obtiene_configuracion().sysbd))):
        print(f' *Encontrada BD en {repositorios.configuracion_repositorio.obtiene_configuracion().sysbd},\
              moviendola a _testing_...')
        shutil.move(normpath(expanduser(repositorios.configuracion_repositorio.obtiene_configuracion().sysbd)),
                    normpath(expanduser('_testing_')))

    print(f' *Generando {repositorios.configuracion_repositorio.obtiene_configuracion().sysbd}')
    print(f' *Agregando "registro de prueba" y "registro de prueba 2"')
    r=modelos.registro_modelo.Registro(nombre='registro de prueba', cuit='20000000000',
                                       detalle='este registro sera borrado',clave='claveinventada')
    repositorios.registros_repositorio.agrega_registro(registro=r,clave=clavedeprueba)
    r=modelos.registro_modelo.Registro(nombre='registro de prueba 2', cuit='20000000000',
                                       detalle='este registro sera borrado',clave='claveinventada')
    repositorios.registros_repositorio.agrega_registro(registro=r,clave=clavedeprueba)

    print(' *Buscando registros por nombre "prueba" :')
    for r in repositorios.registros_repositorio.busca_registro_por_nombre(criterio='prueba', clave=clavedeprueba):
        print(f'  [{r.codigo} {r.nombre} Borrado:{r.borrado}]',end='',flush=True)
    print('')

    print(' *Intercambiando registros...')
    repositorios.registros_repositorio.intercambia_dos_registros(
        repositorios.configuracion_repositorio.obtiene_configuracion().mascara_codigo,
        str(int(repositorios.configuracion_repositorio.obtiene_configuracion().mascara_codigo)+1).zfill(
            len(repositorios.configuracion_repositorio.obtiene_configuracion().mascara_codigo)),
        clave=clavedeprueba)

    print(' *Buscando registros por nombre "registro+prueba"...')
    for r in repositorios.registros_repositorio.busca_registro_por_nombre(criterio='registro+prueba', clave=clavedeprueba):
        print(f'  [{r.codigo} {r.nombre} Borrado:{r.borrado}]', end='', flush=True)
    print('')

    print(' *Buscando registros por CUIT "20000000000"...')
    for r in repositorios.registros_repositorio.busca_registro_por_cuit(criterio='20000000000', clave=clavedeprueba):
        print(f'  [{r.codigo} {r.nombre} Borrado:{r.borrado}]', end='', flush=True)
    print('')

    print(' *Eliminando registros con "prueba" en el nombre...')
    for r in repositorios.registros_repositorio.busca_registro_por_nombre(criterio='prueba', clave=clavedeprueba):
        repositorios.registros_repositorio.borra_registro(codigo=r.codigo,clave=clavedeprueba)

    print(' *Buscando registros por nombre "prueba" nuevamente...')
    for r in repositorios.registros_repositorio.busca_registro_por_nombre(criterio='prueba', clave=clavedeprueba):
        print(f'  [{r.codigo} {r.nombre} Borrado:{r.borrado}]', end='', flush=True)
    if len(repositorios.registros_repositorio.busca_registro_por_nombre(criterio='prueba', clave=clavedeprueba))>0:
        print('')

    print(' *Buscando por nombre "prueba" en registros borrados...')
    for r in repositorios.registros_repositorio.busca_registro_por_nombre(criterio='prueba', clave=clavedeprueba, borrados=True):
        print(f'  [{r.codigo} {r.nombre} Borrado:{r.borrado}]', end='', flush=True)
    print('')

    print(' *Obliterando el registros que contengan "registro de prueba" de la base de datos...')
    for r in repositorios.registros_repositorio.busca_registro_por_nombre(criterio='registro de prueba', clave=clavedeprueba, borrados=True):
        repositorios.registros_repositorio.oblitera_registro(codigo=r.codigo,clave=clavedeprueba)

    print(' *Buscando por nombre "prueba" en registros borrados...')
    for r in repositorios.registros_repositorio.busca_registro_por_nombre(criterio='prueba', clave=clavedeprueba, borrados=True):
        print(f'  [{r.codigo} {r.nombre} Borrado:{r.borrado}]', end='', flush=True)
    print('')

    print(' *Eliminando base de datos temporal...')

    if isfile(normpath(expanduser(repositorios.configuracion_repositorio.obtiene_configuracion().sysbd))):
        os.remove(repositorios.configuracion_repositorio.obtiene_configuracion().sysbd)
    if isfile(normpath(expanduser('_testing_'))):
        shutil.move(normpath(expanduser('_testing_')),repositorios.configuracion_repositorio.obtiene_configuracion().sysbd)


def test_ventana_login():
    vistas.v_login.mostrar()


def test_ventana_crear_clave():
    vistas.v_crearclave.mostrar()


# test_configuracion_repositorio_obtiene_configuracion()
# test_clave_repositorio_registrar_clave()
# test_clave_repositorio_existen_claves()
# test_clave_repositorio_autenticar_clave()
# test_registros_repositorio()
# test_ventana_login()
# test_ventana_crear_clave()
