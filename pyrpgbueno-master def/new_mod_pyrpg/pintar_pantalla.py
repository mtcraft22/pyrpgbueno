import os
import platform
import indicar_acion

import pintar_vara_vida  # importación de módulo para mostrar la vara de vida dinamica


def actualizar_pantalla(escenario, enemigo, jugador, comentario):
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    if escenario.nombre == "combate":
        print(" ")
        print(" ", end="")
        pintar_vara_vida.draw_hp_bar(jugador.vida_max, jugador.vida_act, jugador.nombre)
        print("")
        print(f"                                                             ", end=" ")
        pintar_vara_vida.draw_hp_bar(enemigo.vida_max, enemigo.vida_act, enemigo.nombre)
        print("----------------------------------------------------------------")
        print(f" Piso: {escenario.piso}")
        print("----------------------------------------------------------------")
        print(" Aciones: ")
        a = 1
        for i in escenario.aciones:
            print(" ", a, ". ", i)
            a += 1
        print("----------------------------------------------------------------")
        print(f"Ultimo evento: {comentario}")
        print("----------------------------------------------------------------")
        return indicar_acion.preguntar_acion(escenario.aciones)

    elif escenario.nombre == "tienda":
        escenario.mostrar_items()
        a = 1
        for i in escenario.aciones:
            print(" ", a, ". ", i)
            a += 1
    elif escenario.nombre == "Hub":
        print("seleccione destino: ")
        a = 1
        for i in escenario.aciones:
            print(" ", a, ". ", i)
            a += 1
    elif escenario == "final":
        print(" ")
        print(" ", end="")
        pintar_vara_vida.draw_hp_bar(jugador.vida_max, jugador.vida_act, jugador.nombre)
        print("")
        print(f"                                                             ", end=" ")
        pintar_vara_vida.draw_hp_bar(enemigo.vida_max, enemigo.vida_act, enemigo.nombre)
        print("----------------------------------------------------------------")
        print(f" Piso: {escenario.piso}")
        print("----------------------------------------------------------------")
        print(" Aciones: ")
        a = 1
        for i in escenario.aciones:
            print(" ", a, ". ", i)
            a += 1
        print("----------------------------------------------------------------")
        print(f"Ultimo evento: {comentario}")
        print("----------------------------------------------------------------")




