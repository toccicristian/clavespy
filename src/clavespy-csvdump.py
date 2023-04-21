#!/usr/bin/python3

import modelos.registro_modelo
import repositorios.registros_repositorio
import repositorios.clave_repositorio
import sys


if len(sys.argv)<2 or '=' not in sys.argv[1] or sys.argv[1].split('=')[0] not in ['-p']:
  print(f'Faltan argumentos. \nSintaxis :\n\t {sys.argv[0]} -p=password\n')
  sys.exit()

if not repositorios.clave_repositorio.existen_claves() or not repositorios.clave_repositorio.autenticar_clave(sys.argv[1].split('=')[1]):
  print(f'La clave ingresada no existe en la base de datos.')
  sys.exit()

registros=repositorios.registros_repositorio.leer_bd(clave=sys.argv[1].split('=')[1])

for r in registros:
  if not r.borrado:
    print(f'{r.cuit};{r.nombre};"{r.clave}";"{r.detalle}"')
