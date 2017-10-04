import sys
from Clases import *

Principal = Mega_Man(20, 535, 110, 110,"Imagenes/Inclinado.png")
Enemigo = Enemigo(1500, 535, 130, 130, "Imagenes/Enemigos/Enemigo.png")
Escalera = Escalera(2868,0,40, 650, "Fondo/Escaleras.png")
Fondo = Fondo()
ancho = 1280
alto = 720
ventana = Controlador.configurar_pantalla(ancho, alto)
reloj = Controlador.iniciar_reloj()
colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}
FPS = 20
frames_totales = 0
segundos = 0

Fondos = Colocacion()

while True:

    Acciones(reloj, Principal, FPS, frames_totales, Enemigo, Fondo, Escalera)

    if frames_totales % (FPS / 4) == 0:
        segundos += 0.25

    dibujo(Fondo, ventana, colores)

    frames_totales += 1