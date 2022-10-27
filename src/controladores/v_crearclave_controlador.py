import repositorios.clave_repositorio
import vistas.v_login

def aceptar(v, entry):
    repositorios.clave_repositorio.registrar_clave(entry.get())
    v.destroy()
    vistas.v_login.mostrar()

def cancelar(v):
    v.destroy()

