import math

import colores_e_estilos


# esta parte esta echa por alejandro garcia, esta adaptada a mis nesecidades


def draw_hp_bar(v_max, v_act, nombre, scale=1):
    print(f"{nombre} [", end="")
    color = colores_e_estilos.verde.clear
    p = v_act / v_max
    if p <= 0.2:
        color = colores_e_estilos.rojo.color
    elif p <= 0.5 and p > 0.2:
        color = colores_e_estilos.amarillo.color
    elif p > 0.5:
        color = colores_e_estilos.verde.color
    for i in range(max(math.ceil(v_act / scale), 0)):
        print(color + "█", end=colores_e_estilos.verde.clear)
    for i in range(max(math.floor((v_max - v_act) / scale), 0)):
        print(" ", end="")
    print("] ", end="")
    print(f"{v_act}/{v_max} PS\n")


# Dibuja una barra de magia.
# scale: escala de la barra (a menor valor, más grande será la barra).
'''def draw_mp_bar(self, scale):
    if self.mmp <= 0:
        return
    for i in range(len(self.name) + 1):
        print(" ", end="")
    print("[", end="")
    color = bcolors.BLUE
    p = self.mp / self.mmp
    for i in range(max(math.ceil(self.mp / scale), 0)):
        print(color + "█", end=bcolors.CLEAR)
    for i in range(max(math.floor((self.mmp - self.mp) / scale), 0)):
        print(" ", end="")
    print("] ", end="")
    print(f"{self.mp}/{self.mmp} PM\n")
'''
