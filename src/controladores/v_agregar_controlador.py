import repositorios.registros_repositorio
import modelos.registro_modelo
import vistas.v_error


def agregar_registro(v, e_nombre, e_cuit, e_detalle, e_clave, clavebd=''):
    if len(e_nombre.get())==0:
        vistas.v_error.mostrar(v, mensaje='EL NOMBRE NO PUEDE ESTAR VACÍO')
        return None
    r=modelos.registro_modelo.Registro(nombre=e_nombre.get(),
                                       cuit=e_cuit.get(),
                                       detalle=e_detalle.get(),
                                       clave=e_clave.get())
    repositorios.registros_repositorio.agrega_registro(registro=r,clave=clavebd)
    v.destroy()
