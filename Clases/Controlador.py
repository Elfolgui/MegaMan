import pygame.locals
from .Base import *
from .Bala import Bala


class Controlador(object):

    @classmethod
    def iniciar(cls):
        pygame.init()

    @classmethod
    def terminar(cls):
        pygame.quit()
        quit()

    @classmethod
    def configurar_pantalla(cls, ancho, alto):
        display = pygame.display.set_mode((ancho, alto)) #, pygame.FULLSCREEN
        pygame.display.set_caption("Super MegaMan")
        return display

    @classmethod
    def iniciar_reloj(cls):
        return pygame.time.Clock()

    @classmethod
    def set_fps(cls, reloj, frames):
        reloj.tick(frames)

    @classmethod
    def rellenar_pantalla(cls, ventana, fondo, colores):
        ventana.fill(colores["Negro"])
        ventana.blit(fondo.image, fondo.rect)

    @classmethod
    def mover_pantalla(cls, fondo, Escalera, Enemigo):
        if fondo.rect.x <= 0 and fondo.rect.x > -1200:
            Escalera.rect.x -= 15
            fondo.rect.x -= 15
            Enemigo.rect.x -= 15
        # for item in Base.sprites:
        #     item.rect.x -= 30


    @classmethod
    def buscar_eventos(cls, MegaMan):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cls.terminar()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                cls.terminar()
            if evento.type == pygame.KEYUP:
                MegaMan.detenerse()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and not MegaMan.salto:
                MegaMan.Disparar()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and MegaMan.salto:
                MegaMan.Disparar_Saltando()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
                MegaMan.Agacharse()

    @classmethod
    def Mover_Balas(cls, Grupo):
        for Bala in Grupo:
            if Bala.Tipo == "Bala_Buena":
                if Bala.Direccion:
                    Bala.rect.x += 20
                if not Bala.Direccion:
                    Bala.rect.x -= 20
            if Bala.Tipo == "Bala_Mala":
                if Bala.Estilo == "Recta":
                    Bala.rect.x -= 15
                if Bala.Estilo == "Diagonal":
                    Bala.rect.x -= 15
                    Bala.rect.y -= 12



    @classmethod
    def Mover_Enemigo(cls, Grupo):
        for E in Grupo:
            E.rect.x -= 6

    @classmethod
    def buscar_teclas(cls):
        return pygame.key.get_pressed()

    @classmethod
    def Crear_Bala(cls, MegaMan):
        if MegaMan.Direccion:
            b1 = Bala(MegaMan.rect.x + 55, MegaMan.rect.y + 25, 30, 30, "Balas/Bala.png")
            b1.Direccion = MegaMan.Direccion
            b1.Tipo = "Bala_Buena"
        if not MegaMan.Direccion:
            b1 = Bala(MegaMan.rect.x, MegaMan.rect.y + 30, 30, 30, "Balas/Bala.png")
            b1.Direccion = MegaMan.Direccion
            b1.Tipo = "Bala_Buena"

    @classmethod
    def Eliminar_Enemigo(cls, Enemigo):
        Base.sprites.remove(Enemigo)

    @classmethod
    def salto_MegaMan(cls, MegaMan):
        if MegaMan.salto:
            MegaMan.saltar()

    @classmethod
    def colisiones(cls, MegaMan):
        # Mientras anda a pie
        if MegaMan.salto is False:

            # Hay colision con el piso?
            if MegaMan.colision_piso() is False:

                objeto = MegaMan.colision(Base.bloques)
                if objeto is not False:
                    MegaMan.colision_bloques_caida(objeto)

                # Hay colision con algun bloque?
                # if MegaMan.colision_bloques(objeto):
                #     MegaMan.caerse()

            else:
                if MegaMan.Bajando:
                    MegaMan.detenerse()
                    MegaMan.Bajando = False

            # if MegaMan.colision_Bala() == "Me Pegaron" and Base.sprites.has(Bala):
            #     print("Perdi Vida")
            #     MegaMan.Vida -= 0.5

    #@classmethod
    # def buscar_objetos(cls, mario):
    #     bloque = mario.colision(Base.bloques)
    #     bloque2 = False
    #
    #     if bloque in Base.signos:
    #         bloque2 = mario.colision(Base.ladrillos)
    #         if bloque2 is False:
    #             bloque2 = mario.colision(Base.ladrillos2)
    #     else:
    #         if bloque in Base.ladrillos:
    #             bloque2 = mario.colision(Base.ladrillos2)
    #         elif bloque in Base.ladrillos2:
    #             bloque2 = mario.colision(Base.ladrillos)
    #         if bloque2 is False:
    #             bloque2 = mario.colision(Base.signos)
    #
    #     return bloque, bloque2