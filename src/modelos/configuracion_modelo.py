class Configuracion:
    def __init__(self,sysbd='sys.json',
                 clavebd='clave',
                 temp='tmp',
                 sysbackup='sys.backup',
                 mascara_codigo='00000',
                 ancho_nombre=25,
                 ancho_detalle=40,
                 divisor_linea='=',
                 fuente='Tahoma'):
        self._sysbd=sysbd
        self._clavebd=clavebd
        self._temp=temp
        self._sysbackup=sysbackup
        self._mascara_codigo=mascara_codigo
        self._ancho_nombre=ancho_nombre
        self._ancho_detalle=ancho_detalle
        self._divisor_linea=divisor_linea
        self._fuente=fuente

    @property
    def sysbd(self):
        return self._sysbd

    @sysbd.setter
    def sysbd(self, sysbd):
        self._sysbd = sysbd

    @property
    def clavebd(self):
        return self._clavebd

    @clavebd.setter
    def clavebd(self, clavebd):
        self._clavebd = clavebd

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        self._temp = temp

    @property
    def sysbackup(self):
        return self._sysbackup

    @sysbackup.setter
    def sysbackup(self, sysbackup):
        self._sysbackup = sysbackup

    @property
    def mascara_codigo(self):
        return self._mascara_codigo

    @mascara_codigo.setter
    def mascara_codigo(self,mascara_codigo):
        self._mascara_codigo = mascara_codigo

    @property
    def ancho_nombre(self):
        return self._ancho_nombre

    @ancho_nombre.setter
    def ancho_nombre(self,ancho_nombre):
        self._ancho_nombre = ancho_nombre

    @property
    def ancho_detalle(self):
        return self._ancho_detalle

    @ancho_detalle.setter
    def ancho_detalle(self,ancho_detalle):
        self._ancho_detalle = ancho_detalle

    @property
    def divisor_linea(self):
        return self._divisor_linea

    @divisor_linea.setter
    def divisor_linea(self,divisor_linea):
        self._divisor_linea = divisor_linea

    @property
    def fuente(self):
        return self._fuente

    @fuente.setter
    def fuente(self,fuente):
        self._fuente = fuente
