import pygame
from .Grupos import *


class Base(pygame.sprite.Sprite):

    sprites = Sprites()
    Balas = Sprites()
    Enemigos = Sprites()
    piso = Sprites()
    bloques = Sprites()
    Escalera = Sprites()
    Fondo = Sprites()

    def __init__(self, x, y, ancho, alto, ruta):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(ruta)
        self.image = pygame.transform.scale(self.image, (ancho, alto))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.ancho = ancho
        self.alto = alto
