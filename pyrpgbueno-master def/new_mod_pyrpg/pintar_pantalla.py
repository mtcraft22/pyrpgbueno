import os
import platform

import declaaraciones  # módulo que incluye las instacias de las entidades y objectos
import pintar_vara_vida  # importacion de módulo para mostrar la vara de vida dinamica

piso = 1
aciones = ["atacar", "esquivar", "burla"]


def actualizar_pantalla(aciones, comentario, enemigo, jugador):
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print(" ")
    print(" ", end="")
    pintar_vara_vida.draw_hp_bar()
    print("")
    print("                                           ", " Enemigo:", end=" ")
    pintar_vara_vida.draw_hp_bar()
    print("----------------------------------------------------------------")
    print(f" Piso: {piso}")
    print("----------------------------------------------------------------")
    print(" Aciones: ")
    a = 1
    for i in aciones:
        print(" ", a, ". ", i)
        a += 1
    print("----------------------------------------------------------------")
    print(f"Ultimo evento: {comentario}")
    print("----------------------------------------------------------------")
