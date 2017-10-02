from .Controlador import *
from .Base import Base
import pygame

def Acciones(reloj, MegaMan, FPS, frames_totales, Enemigo, fondo):

    Controlador.set_fps(reloj, FPS)
    Controlador.buscar_eventos(MegaMan)

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        MegaMan.Mov_Derecha(15, frames_totales)

    elif teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        MegaMan.mover_izquierda(15, frames_totales)

    if teclas[pygame.K_w] or teclas[pygame.K_UP] and MegaMan.salto is False:
        MegaMan.activar_salto()

    if frames_totales % 70 == 0 and Enemigo.Activo:
        Enemigo.Disparar()

    if MegaMan.rect.x > 375 and (teclas[pygame.K_d] or teclas[pygame.K_RIGHT]):
        if fondo.rect.x != -1200:
            MegaMan.rect.x = 375
            Controlador.mover_pantalla(fondo)

    if Enemigo.rect.x < 0:
        Controlador.Eliminar_Enemigo(Enemigo)

    if MegaMan.Vida == 0:
        pygame.quit()
        quit()

    Controlador.Mover_Enemigo(Base.Enemigos)
    Controlador.salto_MegaMan(MegaMan)
    MegaMan.colision_Bala()
    Enemigo.Colision_Bala()
    Controlador.Mover_Balas(Base.Balas)
