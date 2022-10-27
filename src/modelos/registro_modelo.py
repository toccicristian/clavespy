class Registro:
    def __init__(self,nombre='',cuit='',detalle='',clave=''):
        self._codigo=''
        self._nombre=nombre
        self._cuit=cuit
        self._detalle=detalle
        self._clave=clave
        self._borrado=False

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def cuit(self):
        return self._cuit

    @cuit.setter
    def cuit(self, cuit):
        self._cuit = cuit

    @property
    def detalle(self):
        return self._detalle

    @detalle.setter
    def detalle(self, detalle):
        self._detalle = detalle

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, clave):
        self._clave = clave

    @property
    def borrado(self):
        return self._borrado

    @borrado.setter
    def borrado(self, borrado):
        self._borrado = borrado
