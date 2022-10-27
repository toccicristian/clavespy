import tkinter as tk
import controladores.v_login_controlador
import repositorios.configuracion_repositorio as conf
import modelos.tooltip_modelo
from os.path import normpath, expanduser


def visibilidad_password(entry_pass, boton_mostrar,img_mostrar_on,img_mostrar_off):
    if entry_pass.cget('show') == '*':
        entry_pass.config(show='')
        boton_mostrar.config(image=img_mostrar_off)
        return None
    entry_pass.config(show='*')
    boton_mostrar.config(image=img_mostrar_on)
    return None


def mostrar(width='450', height='280'):
    fuente=conf.obtiene_configuracion().fuente
    v=tk.Tk()
    v.title('CLAVES PY - LOGIN')
    v.geometry(f'{width}x{height}')
    v.resizable(width=False, height=False)
    marco_titulo=tk.Frame(v)
    img_titulo=tk.PhotoImage(file=normpath(expanduser('./res/user-64px-Freepik.png')))
    label_img_titulo=tk.Label(marco_titulo, image=img_titulo)
    label_titulo=tk.Label(marco_titulo, text='LOGIN', font=(fuente+' ' +str(int(int(width)/(int(height)/20)))))
    marco_entry=tk.Frame(v)
    entry_pass=tk.Entry(marco_entry, show='*', width=f'{int(int(width)/35)}',
                        font=(fuente+' ' +str(int(int(width)/(int(height)/20)))))
    img_boton_mostrar_on=tk.PhotoImage(
        file=normpath(expanduser('./res/eye-64px-Freepik.png')))
    img_boton_mostrar_off=tk.PhotoImage(
        file=normpath(expanduser('./res/hidden-64px-Freepik.png')))

    marco_botones=tk.Frame(v)
    img_boton_login=tk.PhotoImage(
        file=normpath(expanduser('./res/enter-64px-Pixel_perfect.png')))
    img_boton_logout=tk.PhotoImage(file=normpath(expanduser('./res/sign-out-64px-Pixel_perfect.png')))
    boton_mostrar_pass=tk.Button(marco_entry,image=img_boton_mostrar_on,
                                 command = lambda : visibilidad_password(
                                     entry_pass, boton_mostrar_pass,
                                     img_boton_mostrar_on, img_boton_mostrar_off))

    boton_login=tk.Button(marco_botones,image=img_boton_login, command = lambda : controladores.v_login_controlador.login(v,entry_pass))
    boton_cancel=tk.Button(marco_botones, image=img_boton_logout, command = lambda : v.destroy())

    # BINDEOS
    v.bind('<Escape>', lambda event: v.destroy())
    entry_pass.bind('<Return>', lambda event: controladores.v_login_controlador.login(v,entry_pass))
    boton_login.bind('<Return>', lambda event: controladores.v_login_controlador.login(v,entry_pass))


    # PACKS
    marco_titulo.pack(side=tk.TOP,pady=(15,5))
    label_img_titulo.pack(side=tk.LEFT)
    label_titulo.pack(side=tk.LEFT,padx=(10,0),pady=(10,0))
    marco_entry.pack(side=tk.TOP)
    entry_pass.pack(side=tk.LEFT,padx=(10,5),pady=(15,5))
    boton_mostrar_pass.pack(side=tk.LEFT,padx=(5,5),pady=(15,5))
    marco_botones.pack(side=tk.TOP, fill='x')
    boton_login.pack(side=tk.RIGHT,padx=(5,36),pady=(15,5))
    boton_cancel.pack(side=tk.RIGHT,padx=(5,45),pady=(15,5))

    tip_boton_mostrar_pass=modelos.tooltip_modelo.ToolTip(boton_mostrar_pass,'MOSTRAR/OCULTAR CLAVE')
    tip_boton_login=modelos.tooltip_modelo.ToolTip(boton_login,'LOGIN')
    tip_boton_cancel=modelos.tooltip_modelo.ToolTip(boton_cancel,'CANCELAR:        \n Cierra la aplicación.')

    entry_pass.focus_set()
    v.mainloop()

