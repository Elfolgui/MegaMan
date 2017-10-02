import sys
from Clases import *

Principal = Mega_Man(20, 370, 90,90,"Imagenes/Inclinado.png")
Enemigo = Enemigo(1500, 350, 110, 110, "Imagenes/Enemigos/Enemigo.png")
Fondo = Fondo()
ancho = 1280
alto = 720
ventana = Controlador.configurar_pantalla(ancho, alto)
reloj = Controlador.iniciar_reloj()
colores = {"Blanco": (255,255,255), "Negro": (0,0,0)}
FPS = 20
frames_totales = 0
segundos = 0

Colocacion()

while True:

    Acciones(reloj, Principal, FPS, frames_totales, Enemigo, Fondo)

    if frames_totales % (FPS / 4) == 0:
        segundos += 0.25

    dibujo(Fondo, ventana, colores)

    frames_totales += 1