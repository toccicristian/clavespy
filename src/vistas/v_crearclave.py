import tkinter as tk
from os.path import normpath, expanduser
import repositorios.configuracion_repositorio as conf
import modelos.tooltip_modelo
import controladores.v_crearclave_controlador
import constantes.rutas as rutas


def contrasta_claves(entry1,entry2,boton_aceptar):
    if entry1.get() == entry2.get() and len(entry1.get())>0 and len(entry2.get())>0:
        boton_aceptar.config(state='active')
        return None
    boton_aceptar.config(state='disabled')
    return None


def mostrar(width='500', height='450'):
    fuente=conf.obtiene_configuracion().fuente
    v=tk.Tk()
    v.title('CLAVES PY - CREACIÓN DE CLAVE')
    v.geometry(f'{width}x{height}')
    v.resizable(width=False, height=False)
    frame_titulo=tk.Frame(v)
    img_titulo=tk.PhotoImage(file=normpath(expanduser(rutas.ICONO_PASSWORD)))
    label_titulo=tk.Label(frame_titulo,
                          text='CLAVE NO ENCONTRADA',
                          font=(fuente+' ' +str(int(int(width)/(int(height)/20)))))
    label_img_titulo=tk.Label(frame_titulo,image=img_titulo)
    label_claves_titulo=tk.Label(v,text='CREAR NUEVA CLAVE',
                                 font=(fuente+' ' +str(int(int(width)/(int(height)/15)))))
    frame_claves=tk.Frame(v)
    # CLAVE 1
    frame_claves_1=tk.Frame(frame_claves)
    label_claves1=tk.Label(frame_claves_1,text='Ingrese clave: ')
    entry_claves1=tk.Entry(frame_claves_1,show='*',
                           width=f'{int(int(width)/35)}',
                           font=(fuente+' ' +str(int(int(width)/(int(height)/20)))))
    # CLAVE 2
    frame_claves_2=tk.Frame(frame_claves)
    label_claves2=tk.Label(frame_claves_2, text='Repita clave: ')
    entry_claves2=tk.Entry(frame_claves_2,show='*',
                           width=f'{int(int(width)/35)}',
                           font=(fuente+' ' +str(int(int(width)/(int(height)/20)))))

    frame_botones=tk.Frame(v)
    img_boton_cancelar=tk.PhotoImage(file=normpath(expanduser(rutas.ICONO_SIGNOUT)))
    img_boton_aceptar=tk.PhotoImage(file=normpath(expanduser(rutas.ICONO_CHECK)))
    boton_cancelar=tk.Button(frame_botones, image=img_boton_cancelar,
                             command = lambda : controladores.v_crearclave_controlador.cancelar(v))
    boton_aceptar=tk.Button(frame_botones, image=img_boton_aceptar, state='disabled',
                            command = lambda : controladores.v_crearclave_controlador.aceptar(
                                v,entry_claves1))

    # BINDEOS
    v.bind('<Escape>', lambda event: v.destroy())
    entry_claves1.bind('<KeyPress>', lambda event: contrasta_claves(entry_claves1, entry_claves2, boton_aceptar))
    entry_claves2.bind('<KeyPress>', lambda event: contrasta_claves(entry_claves1, entry_claves2, boton_aceptar))
    entry_claves1.bind('<KeyRelease>', lambda event: contrasta_claves(entry_claves1, entry_claves2, boton_aceptar))
    entry_claves2.bind('<KeyRelease>', lambda event: contrasta_claves(entry_claves1, entry_claves2, boton_aceptar))
    boton_aceptar.bind('<Return>', lambda event: controladores.v_crearclave_controlador.aceptar(v, entry_claves1))
    boton_cancelar.bind('<Return>', lambda event: controladores.v_crearclave_controlador.cancelar(v))


    # PACKS
    frame_titulo.pack(side=tk.TOP,pady=(10,30))
    label_titulo.pack(side=tk.LEFT, padx=(5,10), pady=(15,0))
    label_img_titulo.pack(side=tk.LEFT, padx=(10,5), pady=(15,0))
    label_claves_titulo.pack(side=tk.TOP)
    frame_claves.pack(side=tk.TOP, pady=(25,50))
    frame_claves_1.pack(side=tk.TOP,fill=tk.X,pady=(10,10))
    entry_claves1.pack(side=tk.RIGHT)
    label_claves1.pack(side=tk.RIGHT)
    frame_claves_2.pack(side=tk.TOP,fill=tk.X)
    entry_claves2.pack(side=tk.RIGHT)
    label_claves2.pack(side=tk.RIGHT)
    frame_botones.pack(side=tk.TOP,pady=(20,20))
    boton_aceptar.pack(side=tk.RIGHT, padx=(50,0))
    boton_cancelar.pack(side=tk.RIGHT)

    tip_boton_aceptar=modelos.tooltip_modelo.ToolTip(boton_aceptar,'CREAR CLAVE')
    tip_boton_cancelar=modelos.tooltip_modelo.ToolTip(boton_cancelar,'CANCELAR Y CERRAR \nESTA VENTANA            ')

    entry_claves1.focus_set()
    v.mainloop()
