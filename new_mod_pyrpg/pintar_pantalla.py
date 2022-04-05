import os
import platform
import pintar_vara_vida  # importacion de modulo para mostrar la vara de vida dinamica
import classes_entidades

piso = 1
aciones = ["atacar", "esquivar", "burla"]


def actualizar_pantalla(aciones, comentario, enemigo, jugador):
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print(" ")
    print(" ", end="")
    pintar_vara_vida.draw_hp_bar(jugador.vida_maxima,
                                 jugador.Marc.vida_actual,
                                 jugador.Marc.name)
    print("")
    print("                                           ", " Enemigo:", end=" ")
    pintar_vara_vida.draw_hp_bar(enemigo.vida_maxima,
                                 enemigo.vida_actual,
                                 enemigo.Random_tick_speed.name)
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

