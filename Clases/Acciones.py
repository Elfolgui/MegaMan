from .Controlador import *
from .Base import Base
from .Enemigos import Enemigo
import pygame

def Acciones(reloj, MegaMan, FPS, frames_totales, segundos, Enemigo):

    Controlador.set_fps(reloj, FPS)
    Controlador.buscar_eventos(MegaMan)

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        MegaMan.Mov_Derecha(15, frames_totales)

    elif teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        MegaMan.mover_izquierda(15, frames_totales)

    if teclas[pygame.K_w] or teclas[pygame.K_UP] and MegaMan.salto is False:
        MegaMan.activar_salto()

    if segundos == 0.5:
        Enemigo.Disparar()

    if segundos > 0.5:
        Enemigo.Movimiento_Balas()

    Controlador.Mover_Enemigo(Base.Enemigos)
    Controlador.salto_MegaMan(MegaMan)
    Controlador.colisiones(MegaMan)
    Controlador.Mover_Bala(Base.Balas)
