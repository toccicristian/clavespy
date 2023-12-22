import repositorios.configuracion_repositorio as conf
import modelos.ventana_modelo
import modelos.tooltip_modelo
import controladores.v_principal_controlador
from os.path import normpath,expanduser
from herramientas.texto import lista_a_parrafo as l_a_p
import tkinter as tk
from tkinter import ttk
import constantes.rutas as rutas


def mostrar(width='1024', height='600', clave=''):
    fuente=conf.obtiene_configuracion().fuente
    tam_fuente=str(int(int(width)/(int(height)/13)))
    v=tk.Tk()
    v.title('CLAVES PY')
    v.geometry(f'{width}x{height}')
    v.resizable(width=False, height=False)

    f_busqueda=tk.Frame(v)
    l_nombre=tk.Label(f_busqueda,text='Nombre:', font=(fuente+' ' +tam_fuente))
    e_nombre=tk.Entry(f_busqueda,
                      width=f'{int(int(width)/35)}',
                      font=(fuente+' ' +tam_fuente))
    l_cuit=tk.Label(f_busqueda, text='CUIT:', font=(fuente+' ' +tam_fuente))
    e_cuit=tk.Entry(f_busqueda,
                    width=f'{int(int(width)/90)}',
                    font=(fuente+' ' +tam_fuente))

    f_resultados=tk.Frame(v)
    tview_resultados=ttk.Treeview(f_resultados,height=17)
    tview_resultados['columns'] = ('CODIGO','NOMBRE','CUIT','DETALLE','CLAVE')
    tview_resultados.column('#0', width=0, stretch=tk.NO)
    tview_resultados.column('CODIGO', width=0, stretch=tk.NO)
    tview_resultados.column('NOMBRE',anchor=tk.E, stretch=tk.YES, width='310')
    tview_resultados.column('CUIT',anchor=tk.E, stretch=tk.YES, width='100')
    tview_resultados.column('DETALLE',anchor=tk.W, stretch=tk.YES, width='380')
    tview_resultados.column('CLAVE',anchor=tk.W, stretch=tk.YES, width='180')
    tview_resultados.heading('#0', text='', anchor=tk.W)
    tview_resultados.heading('NOMBRE', text='NOMBRE', anchor=tk.W)
    tview_resultados.heading('CUIT', text='CUIT', anchor=tk.W)
    tview_resultados.heading('DETALLE', text='DETALLE', anchor=tk.W)
    tview_resultados.heading('CLAVE', text='CLAVE', anchor=tk.W)
    scrollb_res = tk.Scrollbar(f_resultados, orient='vertical')
    tview_resultados.config(yscrollcommand=scrollb_res.set)
    scrollb_res.config(command=tview_resultados.yview)

    f_panel_inferior=tk.Frame(v)

    f_seleccion = tk.Frame(f_panel_inferior,width=f'{int(int(width)/2)}')
    f_seleccion_nombre = tk.Frame(f_seleccion)
    l_sel_nombre = tk.Label(f_seleccion_nombre, text='NOMBRE:'.rjust(10),width='15')
    e_sel_nombre = tk.Entry(f_seleccion_nombre, text='' ,state='disabled',
                            width=str(int(int(tam_fuente)*1.7)),font=fuente+' '+str(int(int(tam_fuente)/1.5)))
    rmb_sel_nombre = tk.Menu(e_sel_nombre, tearoff=0)
    f_seleccion_cuit = tk.Frame(f_seleccion)
    l_sel_cuit = tk.Label(f_seleccion_cuit, text='CUIT:'.rjust(10),width='15')
    e_sel_cuit = tk.Entry(f_seleccion_cuit,text='' , state='disabled',
                          width=str(int(int(tam_fuente)*1.7)), font=fuente+' '+str(int(int(tam_fuente)/1.5)))
    rmb_sel_cuit = tk.Menu(e_sel_cuit, tearoff=0)
    f_seleccion_detalle = tk.Frame(f_seleccion)
    l_sel_detalle = tk.Label(f_seleccion_detalle, text='DETALLE:'.rjust(10),width='15')
    e_sel_detalle = tk.Entry(f_seleccion_detalle,text='' , state='disabled',
                             width=str(int(int(tam_fuente)*1.7)), font=fuente+' '+str(int(int(tam_fuente)/1.5)))
    rmb_sel_detalle = tk.Menu(e_sel_detalle, tearoff=0)
    f_seleccion_clave = tk.Frame(f_seleccion)
    l_sel_clave = tk.Label(f_seleccion_clave, text='CLAVE:'.rjust(10),width='15')
    e_sel_clave = tk.Entry(f_seleccion_clave,text='' , state='disabled',
                           width=str(int(int(tam_fuente)*1.7)), font=fuente+' '+str(int(int(tam_fuente)/1.5)))
    rmb_sel_clave = tk.Menu(e_sel_clave, tearoff=0)

    f_botones=tk.Frame(f_panel_inferior,width=f'{int(int(width)/2)}')
    img_b_agregar = tk.PhotoImage(file=normpath(expanduser(rutas.ICONO_AGREGAR)))
    b_agregar=tk.Button(f_botones,image=img_b_agregar,
                        command = lambda : controladores.v_principal_controlador.agregar_registro(v, clave))
    img_b_borrar = tk.PhotoImage(file=normpath(expanduser(rutas.ICONO_DELETE)))
    b_borrar=tk.Button(f_botones,image=img_b_borrar,
                       command = lambda : controladores.v_principal_controlador.borrar_registro(
                           v, tview_resultados,clave))
    img_b_swap = tk.PhotoImage(file=normpath(expanduser(rutas.ICONO_REFRESH)))
    b_swap=tk.Button(f_botones,image=img_b_swap)
    img_b_barrer = tk.PhotoImage(file=normpath(expanduser(rutas.ICONO_WIPE)))
    b_barrer=tk.Button(f_botones,image=img_b_barrer)

    # BINDEOS
    v.bind('<Escape>', lambda event: v.destroy())
    e_nombre.bind('<KeyPress>',
                  lambda event : controladores.v_principal_controlador.actualiza_resultados_nombre(
                      e_nombre, tview_resultados, clave))
    e_nombre.bind('<KeyRelease>',
                  lambda event : controladores.v_principal_controlador.actualiza_resultados_nombre(
                      e_nombre, tview_resultados, clave))
    e_cuit.bind('<KeyPress>',
                lambda event : controladores.v_principal_controlador.actualiza_resultados_cuit(
                    e_cuit, tview_resultados, clave))
    e_cuit.bind('<KeyRelease>',
                lambda event : controladores.v_principal_controlador.actualiza_resultados_cuit(
                    e_cuit, tview_resultados, clave))
    tview_resultados.bind('<<TreeviewSelect>>',
                          lambda event : controladores.v_principal_controlador.detalla_elemento(
        tview_resultados,e_sel_nombre,e_sel_cuit,e_sel_detalle,e_sel_clave,clave))

    #RMB EN E_SEL_NOMBRE
    rmb_sel_nombre.add_command(label='Copiar - Ctrl+c',
                               command = lambda : controladores.v_principal_controlador.copiar_a_portapapeles(
                                   v,e_sel_nombre))
    rmb_sel_nombre.bind('<FocusOut>',
                        lambda event : controladores.v_principal_controlador.copiapega_menu_destruye(
                            rmb_sel_nombre, event=None))
    e_sel_nombre.bind('<Button-3>',
                      lambda event : controladores.v_principal_controlador.copiapega_menu(event, rmb_sel_nombre))

    #RMB EN E_SEL_CUIT
    rmb_sel_cuit.add_command(label='Copiar - Ctrl+c',
                               command = lambda : controladores.v_principal_controlador.copiar_a_portapapeles(
                                   v,e_sel_cuit))
    rmb_sel_cuit.bind('<FocusOut>',
                        lambda event : controladores.v_principal_controlador.copiapega_menu_destruye(
                            rmb_sel_cuit, event=None))
    e_sel_cuit.bind('<Button-3>',
                      lambda event : controladores.v_principal_controlador.copiapega_menu(event, rmb_sel_cuit))

    #RMB EN E_SEL_DETALLE
    rmb_sel_detalle.add_command(label='Copiar - Ctrl+c',
                               command = lambda : controladores.v_principal_controlador.copiar_a_portapapeles(
                                   v,e_sel_detalle))
    rmb_sel_detalle.bind('<FocusOut>',
                        lambda event : controladores.v_principal_controlador.copiapega_menu_destruye(
                            rmb_sel_detalle, event=None))
    e_sel_detalle.bind('<Button-3>',
                      lambda event : controladores.v_principal_controlador.copiapega_menu(event, rmb_sel_detalle))

    #RMB EN E_SEL_CLAVE
    rmb_sel_clave.add_command(label='Copiar - Ctrl+c',
                               command = lambda : controladores.v_principal_controlador.copiar_a_portapapeles(
                                   v,e_sel_clave))
    rmb_sel_clave.bind('<FocusOut>',
                        lambda event : controladores.v_principal_controlador.copiapega_menu_destruye(
                            rmb_sel_clave, event=None))
    e_sel_clave.bind('<Button-3>',
                      lambda event : controladores.v_principal_controlador.copiapega_menu(event, rmb_sel_clave))

    # PACK
    f_busqueda.pack(side=tk.TOP,pady=(20,10))
    l_nombre.pack(side=tk.LEFT)
    e_nombre.pack(side=tk.LEFT, padx=(0,75))
    l_cuit.pack(side=tk.LEFT, padx=(10,0))
    e_cuit.pack(side=tk.LEFT)
    f_resultados.pack(side=tk.TOP,padx=(5,5))
    tview_resultados.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
    scrollb_res.pack(side=tk.RIGHT, fill=tk.BOTH)
    f_panel_inferior.pack(side=tk.TOP,fill=tk.X,padx=(6,5),pady=(20,20))
    f_seleccion.pack(side=tk.LEFT)
    f_seleccion_nombre.pack(side=tk.TOP, fill=tk.X)
    l_sel_nombre.pack(side=tk.LEFT)
    e_sel_nombre.pack(side=tk.LEFT)
    f_seleccion_cuit.pack(side=tk.TOP, fill=tk.X)
    l_sel_cuit.pack(side=tk.LEFT)
    e_sel_cuit.pack(side=tk.LEFT)
    f_seleccion_detalle.pack(side=tk.TOP, fill=tk.X)
    l_sel_detalle.pack(side=tk.LEFT)
    e_sel_detalle.pack(side=tk.LEFT)
    f_seleccion_clave.pack(side=tk.TOP, fill=tk.X)
    l_sel_clave.pack(side=tk.LEFT)
    e_sel_clave.pack(side=tk.LEFT)
    f_botones.pack(side=tk.LEFT,padx=(85,10))
    b_agregar.pack(side=tk.LEFT,padx=(5,5))
    b_borrar.pack(side=tk.LEFT,padx=(5,5))
    b_swap.pack(side=tk.LEFT,padx=(85,5))
    b_barrer.pack(side=tk.RIGHT,padx=(5,5))

    tip_boton_agregar=modelos.tooltip_modelo.ToolTip(
        b_agregar, l_a_p(['AGREGA UN','REGISTRO A LA BD']))

    tip_boton_borrar=modelos.tooltip_modelo.ToolTip(
        b_borrar, l_a_p(['BORRA UN REGISTRO','DE LA BD']))

    tip_boton_swap=modelos.tooltip_modelo.ToolTip(
        b_swap, l_a_p(['INTERCAMBIA DOS','REGISTROS SELECCIONADOS']))

    tip_boton_barrer=modelos.tooltip_modelo.ToolTip(
        b_barrer, l_a_p(['OBLITERA TODOS LOS','REGISTROS BORRADOS','DE LA BD']))

    e_nombre.focus_set()
    v.mainloop()
