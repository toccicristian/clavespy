#!/usr/bin/python3

import modelos.registro_modelo
import repositorios.registros_repositorio
import repositorios.clave_repositorio
import herramientas.argumentos as h_argumentos
import sys

ayuda_clavespy_csvdump=f"""
  Imprime campos de los registros de la base datos de clavespy en formato csv.

  SINTAXIS : {sys.argv[0]} [argumentos]

  Argumentos:
    -p=password       Introduce la clave para acceder a la base de datos.
    -v                Imprime el digito verificador junto a cada registro.
    -h/--help/--ayuda Imprime ayuda del script y sale.

"""

argumentos_de_ayuda=['-h','--help','--ayuda']

if len(sys.argv)<2 or not h_argumentos.existe_al_menos_uno(argumentos=['-p']+argumentos_de_ayuda,buscar_en_lista=sys.argv):
  print('Faltan argumentos o no son validos. \n'+ayuda_clavespy_csvdump)
  sys.exit()

if h_argumentos.existe_al_menos_uno(argumentos=argumentos_de_ayuda,buscar_en_lista=sys.argv):
  print(ayuda_clavespy_csvdump)
  sys.exit()

if not repositorios.clave_repositorio.existen_claves() or not repositorios.clave_repositorio.autenticar_clave(h_argumentos.busca_argumento(argumentos=sys.argv, argumento='-p')):
  print(f'La clave ingresada no existe en la base de datos.')
  sys.exit()

registros=repositorios.registros_repositorio.leer_bd(clave=h_argumentos.busca_argumento(argumentos=sys.argv, argumento='-p'))

if h_argumentos.existe_argumento(argumentos=sys.argv,argumento='-v'):
  for reg in [r for r in registros if not r.borrado]:
    print(f'"{reg.cuit[-1::]}";{reg.cuit};{reg.nombre};"{reg.clave}";"{reg.detalle}')
  sys.exit()

for reg in [r for r in registros if not r.borrado]:
  print(f'{reg.cuit};{reg.nombre};"{reg.clave}";"{reg.detalle}"')
