from .Controlador import *
from .Controlador_Personajes import *
from .Base import Base
import pygame

def Acciones(reloj, MegaMan, FPS, frames_totales, Enemigo, fondo, Escalera):

    Controlador.set_fps(reloj, FPS)
    Controlador.buscar_eventos(MegaMan)

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        MegaMan.Mov_Derecha(15, frames_totales)

    elif teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        MegaMan.Mov_Izquierda(15, frames_totales)

    if teclas[pygame.K_w] or teclas[pygame.K_UP] and MegaMan.salto is False:
        MegaMan.activar_salto()

    if frames_totales % 70 == 0 and Enemigo.Activo:
        Enemigo.Disparar()

    if MegaMan.rect.x > 375 and (teclas[pygame.K_d] or teclas[pygame.K_RIGHT]):
        if fondo.rect.x > -1700:
            MegaMan.rect.x = 375
            Controlador.mover_pantalla(fondo, Escalera, Enemigo, Base.Balas)

    if Enemigo.rect.x < 0:
        Controlador.Eliminar_Enemigo(Enemigo)

    if MegaMan.Vida == 0:
        pygame.quit()
        quit()

    if MegaMan.Colision_Escalera(Base.Escalera) and (teclas[pygame.K_w] or teclas[pygame.K_UP]):
        MegaMan.rect.y -= 15

    Controlador_Personajes.Mover_Enemigo()
    Controlador_Personajes.salto_MegaMan(MegaMan)
    Controlador_Personajes.Colisiones()
    Controlador.Mover_Balas(Base.Balas)
