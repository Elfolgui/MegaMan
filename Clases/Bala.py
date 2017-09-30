from .Base import *

class Bala(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)
        self.Direccion = False
        self.Tipo = ""
        self.Estilo = ""
        Base.Balas.add(self)
        Base.sprites.add(self)