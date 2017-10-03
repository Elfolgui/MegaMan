from .Base import *

class Escalera(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)
        Base.Escalera.add(self)
        self.Tipo = "Escalera"