from .Base import Base
from .Bala import Bala
import pygame

class Enemigo(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)
        self.Lista_Balas = []
        self.Activo = True
        self.Tipo = "Enemigo"
        Base.sprites.add(self)
        Base.Enemigos.add(self)

    def Disparar(self):
        b1 = Bala(self.rect.x, self.rect.y + 50, 30, 30, "Balas/Bala.png")
        b2 = Bala(self.rect.x, self.rect.y + 50, 30, 30, "Balas/Bala.png")
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
        Disparo = self.colision(Base.Balas)
        if Disparo is not False and Disparo.Tipo == "Bala_Buena":
            print(Disparo)
            print("Choque")
            print(Base.sprites.sprites())
            self.Activo = False
            Base.sprites.remove(Disparo)
            Base.sprites.remove(self)
            Base.Balas.remove(Disparo)
            Base.Enemigos.remove(self)
            print(Base.sprites.sprites())