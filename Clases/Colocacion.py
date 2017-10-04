from .Piso import *

# Separacion entre bloques de piso: 72

def Colocacion():

    # CREACION DE PISO

    x = 0

    for i in range(21):
        piso = Piso(x,630)
        x += 119

    # """x = 4320
    #
    # for i in range(17):
    #     piso = Piso(x,695)
    #     x += 72
    #
    # x = 5760
    #
    # for i in range(6):
    #     piso = Piso(x,695)
    #     x += 72"""