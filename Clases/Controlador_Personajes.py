import pygame
from .Base import *


class Controlador_Personajes(object):

    @classmethod
    def Colisiones(cls):
        for E in Base.Enemigos:
            E.Colision_Bala()
        for P in Base.Principales:
            P.Colision_Enemigo()
            P.colision_Bala()

    @classmethod
    def salto_MegaMan(cls, MegaMan):
        if MegaMan.salto:
            MegaMan.saltar()

    @classmethod
    def Mover_Enemigo(cls):
        for E in Base.Enemigos:
            E.rect.x -= 6