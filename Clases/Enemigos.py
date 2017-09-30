from .Base import Base
from .Bala import Bala

class Enemigo(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)
        self.Lista_Balas = []
        Base.sprites.add(self)
        Base.Enemigos.add(self)

    def Disparar(self):
        b1 = Bala(self.rect.x, self.rect.y + 30, 30, 30, "Balas/Bala.png")
        b2 = Bala(self.rect.x, self.rect.y + 30, 30, 30, "Balas/Bala.png")
        b1.Tipo = "Bala_Mala"
        b2.Tipo = "Bala_Mala"
        b1.Estilo = "Diagonal"
        b2.Estilo = "Recta"