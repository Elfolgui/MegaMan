from .Base import *

class Bala_Mala(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)
        Base.Balas_Malas.add(self)
        Base.sprites.add(self)