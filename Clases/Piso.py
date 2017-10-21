from .Base import *

ancho = 1280
alto = 720

class Piso(Base):

    def __init__(self, x, y):
        Base.__init__(self, x, y, 119, 90, "imagenes/Bloque.png")
        Base.sprites.add(self)
        Base.piso.add(self)