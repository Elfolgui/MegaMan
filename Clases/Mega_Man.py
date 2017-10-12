import pygame
from .Base import Base
from .Controlador import Controlador

class Mega_Man(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)
        self.Movimientos = ("Movimientos/Entrando_1.png", "Movimientos/Entrando_2.png", "Movimientos/Entrando_3.png",
                            "Movimientos/Inclinado.png", "Movimientos/P_Paso.png", "Movimientos/P_Derecho.png",
                            "Movimientos/P_Paso.png", "Movimientos/P_Izquierdo.png", "Movimientos/Saltando.png",
                            "Movimientos/Disparando.png", "Movimientos/Disparando_Aire.png")

        self.Tipo = "Principal"
        self.frame = 0
        self.Estado = 5
        self.maximo = 0
        self.Entrada = True
        self.Direccion = True
        self.Bajando = False
        self.salto = False
        self.Vida = 3
        Base.sprites.add(self)
        Base.Principales.add(self)

    # def Primera_Animacion(self):
    #     if self.Entrada:
    #         if self.rect.x < 585:
    #             while self.Estado < 3:
    #                 print(self.Estado)
    #                 self.cambiar_sprite(self.Movimientos[self.Estado])
    #                 self.rect.x += 25
    #                 self.Estado += 1
    #         if self.rect.x == 585:
    #             self.Entrada = False

    def Mov_Derecha(self, velocidad, frames_Totales):

        if not self.Direccion:
            self.Direccion = True
            self.invertir()
            self.Estado = 3
            return

        if not self.salto:
            if (frames_Totales - self.frame) > 2:

                if self.Estado == 3 or self.Estado == 4 or self.Estado == 5 or self.Estado == 6:
                    self.Estado += 1
                    self.frame = frames_Totales
                    self.cambiar_sprite(self.Movimientos[self.Estado])

                elif self.Estado == 7:
                    self.Estado = 4
                    self.frame = frames_Totales
                    self.cambiar_sprite(self.Movimientos[self.Estado])

        self.rect.x += velocidad

    def Mov_Izquierda(self, velocidad, frames_Totales):

        if self.Direccion:
            self.Direccion = False
            self.invertir()
            self.Estado = 3
            return

        if not self.salto:
            if (frames_Totales - self.frame > 2):

                if self.Estado == 3 or self.Estado == 4 or self.Estado == 5 or self.Estado == 6:
                    self.Estado += 1
                    self.frame = frames_Totales
                    self.cambiar_sprite(self.Movimientos[self.Estado])
                    self.invertir()

                elif self.Estado == 7:
                    self.Estado = 4
                    self.frame = frames_Totales
                    self.cambiar_sprite(self.Movimientos[self.Estado])
                    self.invertir()

        self.rect.x -= velocidad

    def Agacharse(self):
        if self.Direccion:
            self.cambiar_sprite(self.Movimientos[8])
        if not self.Direccion:
            self.cambiar_sprite(self.Movimientos[8])
            self.invertir()

    def activar_salto(self):
        self.original = self.rect.y
        self.maximo = self.rect.y - 150
        self.salto = True
        self.cambiar_sprite(self.Movimientos[8])
        if self.Direccion is False:
            self.invertir()

    def saltar(self):

        if self.maximo == self.rect.y:
            self.Bajando = True

        if self.Bajando is False:

            if self.rect.y <= self.maximo + 60:
                self.rect.y -= 10
            else:
                self.rect.y -= 20

        if self.Bajando is True:
            self.rect.y += 20

        if self.colision_piso():
            print(self.rect.y)
            self.terminar_salto()

    def Disparar(self):
        if self.Direccion:
            self.cambiar_sprite(self.Movimientos[9])
            Controlador.Crear_Bala(self)
        else:
            self.cambiar_sprite(self.Movimientos[9])
            self.invertir()
            Controlador.Crear_Bala(self)

    def Disparar_Saltando(self):
        if self.Direccion:
            self.cambiar_sprite(self.Movimientos[10])
            Controlador.Crear_Bala(self)
        else:
            self.cambiar_sprite(self.Movimientos[10])
            self.invertir()
            Controlador.Crear_Bala(self)

    def cambiar_sprite(self, movimiento):
        self.image = pygame.image.load(movimiento)
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))

    def invertir(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))

    def detenerse(self):
        if self.salto is False:
            self.cambiar_sprite(self.Movimientos[3])
            if self.Direccion is False:
                self.invertir()

    def colision(self, grupo):
        elemento = pygame.sprite.spritecollideany(self, grupo, collided=None)
        if elemento is not None:
            return elemento
        else:
            return False

    def Colision_Escalera(self, Grupo):
        if self.colision(Grupo) is not False:
            return True

    def colision_piso(self):
        if self.colision(Base.piso) is False:
            return False
        return True

    def colision_Bala(self):
        Bala = self.colision(Base.Balas)
        if Bala is not False and Bala.Tipo == "Bala_Mala":
            print("Toque Bala")
            Base.sprites.remove(Bala)
            Base.Balas.remove(Bala)
            self.Vida -= 1

    def Colision_Enemigo(self):
        Enemigo = self.colision(Base.Enemigos)
        if Enemigo is not False:
            print("Toque Enemigo")
            self.Vida -= 1




    # def colision_bloques_caida(self, bloque):
    #     if self.rect.x < bloque.rect.x + 60 and self.rect.x > bloque.rect.x - 90:
    #         # Chocó estando sobre el bloque?
    #         if bloque.rect.y == self.rect.y + 100:
    #             self.terminar_salto()

            # Chocó estando fuera de la hitbox?
            # Chocó en la derecha?
            # elif self.rect.x > bloque.rect.x:
            #     self.rect.x = bloque.rect.x + 70
            # # Chocó en la izquierda?
            # elif self.rect.x < bloque.rect.x:
            #     self.rect.x = bloque.rect.x - 95

    def terminar_salto(self):
        if self.Bajando:
            self.Bajando = False
            self.salto = False
            self.detenerse()

    # def colisiones_con_salto(self):
    #
    #     if self.colision(Base.piso) is not False:
    #         print("Toque Bloque")
    #         print(self.rect.y)
    #         self.terminar_salto()
            # Colisiona con dos objetos?
        # bloque, bloque2 = Controlador.buscar_objetos(self)
        #
        # if bloque2 is not False:
        #     # Cuál está mas cerca de rect.x
        #     comparacion = self.rect.x - bloque.rect.x
        #     comparacion2 = self.rect.x - bloque2.rect.x
        #     if comparacion < 0:
        #         comparacion = comparacion + -(comparacion) + comparacion
        #     if comparacion2 < 0:
        #         comparacion2 = comparacion2 + comparacion2 + comparacion2
        #     if comparacion > comparacion2:
        #         bloque = bloque2

        # Chocó con un bloque?
        # if bloque is not False:
        #     self.colision_bloques_salto(bloque)
