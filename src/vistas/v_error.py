import tkinter as tk
import repositorios.configuracion_repositorio as conf


def mostrar(parent,mensaje='',width='300', height='180', titulo='CLAVES PY - ERROR!!!'):
    fuente=conf.obtiene_configuracion().fuente
    tam_fuente=str(int(int(width)/(int(height)/13)))
    v=tk.Toplevel(parent)
    v.title(titulo)
    v.geometry(f'{width}x{height}')
    v.resizable(width=False, height=False)
    l_mensaje=tk.Label(v, text=mensaje)
    b_aceptar=tk.Button(v, text='ACEPTAR', command = lambda : v.destroy())

    b_aceptar.bind('<Return>', lambda event : v.destroy())
    v.bind('<Escape>', lambda event : v.destroy())
    v.bind('<Return>', lambda event : v.destroy())
    v.bind('<space>', lambda event : v.destroy())

    l_mensaje.pack(side=tk.TOP, pady=(20,10))
    b_aceptar.pack(side=tk.BOTTOM, pady=(10,20))
