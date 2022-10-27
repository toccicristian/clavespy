import tkinter as tk

class Messagebox:
    def __init__(self,
                 parent=None,titulo='ERROR',
                 mensaje='ERROR',
                 texto_aceptar='Aceptar',
                 ancho='300',alto='100'):
        if parent is None:
            return parent
        self._v=tk.Toplevel(parent)
        self._v.title(titulo)
        self._v.geometry(f'{ancho}x{alto}')
        self._lbl_msg=tk.Label(self._v, text=mensaje)
        self._b_aceptar=tk.Button(self._v, text=texto_aceptar,
                                  command=lambda: self._v.destroy())
        self._lbl_msg.pack(side=tk.TOP,
                           padx=(5,5),
                           pady=(10,10))
        self._b_aceptar.pack(side=tk.TOP,
                             anchor=tk.E,
                             padx=(5,5),
                             pady=(10,10))
        self._v.bind('<Escape>', lambda event: self._v.destroy())
        self._v.focus_set()

