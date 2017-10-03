from . import *

def dibujo(fondo, ventana, colores):

    Controlador.rellenar_pantalla(ventana, fondo, colores)
    Base.Escalera.draw(ventana)
    Base.sprites.draw(ventana)
    pygame.display.flip()