import repositorios.registros_repositorio as reg_repo
import repositorios.clave_repositorio
import vistas.v_agregar
import vistas.v_error
import tkinter as tk

def actualiza_tview(resultados,tview):
    tview.delete(*tview.get_children())
    i=0
    for reg in resultados:
        tview.insert(parent='', index=i, iid=i, text='',
                     values=(reg.codigo ,reg.nombre,reg.cuit,reg.detalle,reg.clave))
        i+=1


def actualiza_resultados_cuit(entry,tview,clave):
    resultados=reg_repo.busca_registro_por_cuit(criterio=entry.get(),clave=clave)
    actualiza_tview(resultados,tview)
    del resultados


def actualiza_resultados_nombre(entry,tview,clave):
    resultados=reg_repo.busca_registro_por_nombre(criterio=entry.get(),clave=clave)
    actualiza_tview(resultados,tview)
    del resultados


def actualiza_entry(entry,texto):
    entry.configure(state='normal')
    entry.delete(0,tk.END)
    entry.insert(0,texto)
    entry.configure(state='readonly')


def detalla_elemento(tview,e_nombre,e_cuit,e_detalle,e_clave,clave):
    if not tview.selection():
        return False
    actualiza_entry(e_nombre,f'{tview.item(tview.focus())["values"][1]}')
    actualiza_entry(e_cuit,f'{tview.item(tview.focus())["values"][2]}')
    actualiza_entry(e_detalle,f'{tview.item(tview.focus())["values"][3]}')
    actualiza_entry(e_clave,reg_repo.busca_registro_por_codigo(tview.item(tview.focus())["values"][0],clave).clave)


def copiapega_menu(event, menu):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()


def copiapega_menu_destruye(menu, event=None):
    menu.unpost()


def copiar_a_portapapeles(v,entry):
    texto = entry.get()
    if entry.select_present():
        texto = entry.selection_get()
    v.clipboard_clear()
    v.clipboard_append(texto)


def agregar_registro(parent, clavebd=''):
    if repositorios.clave_repositorio.autenticar_clave(clavebd):
        vistas.v_agregar.mostrar(parent,clavebd=clavebd)

    return None


def borrar_registro(parent, tview, clavebd=''):
    if not tview.selection():
        return False

    nombre_reg=tview.item(tview.focus())['values'][1]
    repositorios.registros_repositorio.borra_registro(
        codigo=tview.item(tview.focus())['values'][0],clave=clavebd)
    vistas.v_error.mostrar(parent=parent,
                   mensaje=f'El registro para \n{nombre_reg}\
                   \nha sido borrado', titulo='CLAVES PY - ATENCION!!!!')


