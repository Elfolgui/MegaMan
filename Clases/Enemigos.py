from .Base import Base
from .Bala_Mala import Bala_Mala


class Enemigo(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)
        self.Lista_Balas = []
        Base.sprites.add(self)
        Base.Enemigos.add(self)

    def Disparar(self):
        b1 = Bala_Mala(self.rect.x, self.rect.y + 30, 30, 30, "Balas/Bala.png")
        b2 = Bala_Mala(self.rect.x, self.rect.y + 30, 30, 30, "Balas/Bala.png")
        self.Lista_Balas.append(b1)
        self.Lista_Balas.append(b2)

    def Movimiento_Balas(self):
        #Esto tiene que recorrer la lista de balas y llamar a sus métodos de movimientos