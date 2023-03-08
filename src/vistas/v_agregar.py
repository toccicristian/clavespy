import tkinter as tk
from os.path import normpath,expanduser
import repositorios.configuracion_repositorio as conf
import controladores.v_agregar_controlador
import constantes.rutas as rutas

def mostrar(toplevel, width='500', height='400', clavebd=''):
    fuente=conf.obtiene_configuracion().fuente
    tam_fuente=str(int(int(width)/(int(height)/13)))
    v=tk.Toplevel(toplevel)
    v.title('CLAVES PY - AGREGAR REGISTRO')
    v.geometry(f'{width}x{height}')
    v.resizable(width=False, height=False)

    f_titulo=tk.Frame(v)

    img_titulo_agregar=tk.PhotoImage(file=normpath(expanduser(rutas.ICONO_NOTA)))
    l_img_titulo_agregar=tk.Label(f_titulo, image=img_titulo_agregar)
    l_img_titulo_agregar.image=img_titulo_agregar
    l_titulo_agregar=tk.Label(f_titulo, text='Agregar a BD', font=fuente+' '+tam_fuente)

    f_ingreso=tk.Frame(v)
    f_nombre=tk.Frame(f_ingreso)
    l_nombre=tk.Label(f_nombre, text='NOMBRE:', font=fuente+' '+tam_fuente)
    e_nombre=tk.Entry(f_nombre,
                      width=f'{int(int(width)/20)}',
                      font=(fuente+' ' +tam_fuente)
                      )
    f_cuit=tk.Frame(f_ingreso)
    l_cuit=tk.Label(f_cuit, text='CUIT:', font=fuente+' '+tam_fuente)
    e_cuit=tk.Entry(f_cuit,
                    width=f'{int(int(width)/20)}',
                    font=(fuente+' ' +tam_fuente)
                    )
    f_detalle=tk.Frame(f_ingreso)
    l_detalle=tk.Label(f_detalle, text='DETALLE:', font=fuente+' '+tam_fuente)
    e_detalle=tk.Entry(f_detalle,
                    width=f'{int(int(width)/20)}',
                    font=(fuente+' ' +tam_fuente)
                    )
    f_clave=tk.Frame(f_ingreso)
    l_clave=tk.Label(f_clave, text='CLAVE:', font=fuente+' '+tam_fuente)
    e_clave=tk.Entry(f_clave,
                    width=f'{int(int(width)/20)}',
                    font=(fuente+' ' +tam_fuente)
                    )
    f_botones=tk.Frame(v, width=f'{int(int(width)/2)}')
    img_b_agregar = tk.PhotoImage(file=normpath(expanduser(rutas.ICONO_AGREGAR)))
    b_agregar=tk.Button(f_botones,image=img_b_agregar,
                       command = lambda : controladores.v_agregar_controlador.agregar_registro(
                           v, e_nombre, e_cuit, e_detalle, e_clave, clavebd))
    b_agregar.image=img_b_agregar
    img_b_cancelar=tk.PhotoImage(file=normpath(expanduser(rutas.ICONO_SIGNOUT)))
    b_cancelar=tk.Button(f_botones, image=img_b_cancelar,command = lambda : v.destroy())
    b_cancelar.image=img_b_cancelar
    #BINDEOS
    v.bind('<Escape>', lambda event: v.destroy())
    b_agregar.bind('<Return>', lambda event: controladores.v_agregar_controlador.agregar_registro(
        v, e_nombre, e_cuit, e_detalle, e_clave, clavebd))
    #PACKING
    f_titulo.pack(side=tk.TOP,pady=(10,10))
    l_img_titulo_agregar.pack(side=tk.LEFT)
    l_titulo_agregar.pack(side=tk.LEFT)
    f_ingreso.pack(side=tk.TOP, fill=tk.X)
    f_nombre.pack(side=tk.TOP,pady=(10,5), fill=tk.X, padx=(0,int(int(width)/10)))
    e_nombre.pack(side=tk.RIGHT)
    l_nombre.pack(side=tk.RIGHT)
    f_cuit.pack(side=tk.TOP,pady=(5,5), fill=tk.X, padx=(0,int(int(width)/10)))
    e_cuit.pack(side=tk.RIGHT)
    l_cuit.pack(side=tk.RIGHT)
    f_detalle.pack(side=tk.TOP,pady=(5,5), fill=tk.X, padx=(0,int(int(width)/10)))
    e_detalle.pack(side=tk.RIGHT)
    l_detalle.pack(side=tk.RIGHT)
    f_clave.pack(side=tk.TOP,pady=(5,10), fill=tk.X, padx=(0,int(int(width)/10)))
    e_clave.pack(side=tk.RIGHT)
    l_clave.pack(side=tk.RIGHT)
    f_botones.pack(side=tk.TOP, fill=tk.X, padx=(0,int(int(width)/10)), pady=(20,0))
    b_agregar.pack(side=tk.RIGHT, padx=(50,int(int(width)/5)))
    b_cancelar.pack(side=tk.RIGHT, padx=(50,0))

    e_nombre.focus_set()
