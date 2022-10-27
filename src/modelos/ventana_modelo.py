import tkinter as tk

class Ventana:
    def __init__(self,parent=None,
                 titulo='.set_titulo(str)',
                 ancho='800',alto='600'):
        self._parent=parent
        self._ventana=tk.Tk()
        if self._parent is not None:
            self._ventana=tk.Toplevel(parent)
        self._ventana.title(titulo)
        self._ventana.geometry(f'{ancho}x{alto}')

    def cerrar(self):
        if self._parent is None:
            import sys
            sys.exit()
            #self._ventana.destroy()

    def iniciar(self):
        if self._parent is None:
            self._ventana.mainloop()
            return None
        self._ventana.pack()

    def get_ventana(self):
        return self._ventana
