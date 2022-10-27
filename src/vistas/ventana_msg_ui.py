import modelos.ventana_msg_modelo

def mostrar(parent=None,
            titulo='',
            mensaje='',
            texto_boton=''):
    v=modelos.ventana_msg_modelo.Messagebox(
        parent=parent, titulo=titulo,
        mensaje=mensaje,
        texto_aceptar=texto_boton)
