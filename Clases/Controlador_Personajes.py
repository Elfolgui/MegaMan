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
            if P.salto is False:
                if P.colision_piso():
                    print("Colisione")
                    if P.Bajando:
                        P.detenerse()
                        P.Bajando = False

    @classmethod
    def colisiones(cls, MegaMan):
        if MegaMan.salto is False:
            if MegaMan.colision_piso():
                print("Colisione")
                if MegaMan.Bajando:
                    MegaMan.detenerse()
                    MegaMan.Bajando = False
                    # Hay colision con el piso?
                    # if MegaMan.colision_piso() is False:
                    #     objeto = MegaMan.colision(Base.bloques)
                    #     if objeto is not False:
                    #         MegaMan.colision_bloques_caida(objeto)
    # @classmethod
    # def MegaMan_Entrada(cls, MegaMan):
    #     for Num in range(3):
    #         MegaMan.cambiar_Sprite(MegaMan.Estado[Num])

    @classmethod
    def salto_MegaMan(cls, MegaMan):
        if MegaMan.salto:
            MegaMan.saltar()

    @classmethod
    def Mover_Enemigo(cls):
        for E in Base.Enemigos:
            E.rect.x -= 6