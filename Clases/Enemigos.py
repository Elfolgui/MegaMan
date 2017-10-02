from .Base import Base
from .Bala import Bala
import pygame

class Enemigo(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)
        self.Lista_Balas = []
        self.Activo = True
        Base.sprites.add(self)
        Base.Enemigos.add(self)

    def Disparar(self):
        b1 = Bala(self.rect.x, self.rect.y + 30, 30, 30, "Balas/Bala.png")
        b2 = Bala(self.rect.x, self.rect.y + 30, 30, 30, "Balas/Bala.png")
        b1.Tipo = "Bala_Mala"
        b2.Tipo = "Bala_Mala"
        b1.Estilo = "Diagonal"
        b2.Estilo = "Recta"

    def colision(self, grupo):
        elemento = pygame.sprite.spritecollideany(self, grupo, collided=None)
        if elemento is not None:
            return elemento
        else:
            return False

    def Colision_Bala(self):
        Bala = self.colision(Base.Balas)
        if Bala is not False and Bala.Tipo == "Bala_Buena":
            self.Activo = False
            Base.sprites.remove(Bala)
            Base.sprites.remove(self)
            Base.Balas.remove(Bala)
            Base.Enemigos.remove(self)
