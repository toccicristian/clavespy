import repositorios.clave_repositorio
import vistas.v_principal
import herramientas.encriptacion as encript

def login (v, entry_pass):
    if repositorios.clave_repositorio.autenticar_clave(entry_pass.get()):
        entry_pass_get=entry_pass.get()
        v.destroy()
        vistas.v_principal.mostrar(clave=entry_pass_get)
        return None
    return None

