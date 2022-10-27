#!/usr/bin/python3

import sys
import controladores.v_login_controlador
import repositorios.clave_repositorio
import vistas.v_crearclave
import vistas.v_login


if not repositorios.clave_repositorio.existen_claves():
    vistas.v_crearclave.mostrar()
    sys.exit()

vistas.v_login.mostrar()
