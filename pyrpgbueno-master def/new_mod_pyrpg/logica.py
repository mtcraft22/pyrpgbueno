import random


import declaaraciones
import lista_enemigos_por_nivel
import pintar_pantalla
import indicar_acion
from classes.classes_objetos import lista_items as productos


def combate():
    ene = random.choice(lista_enemigos_por_nivel.sacar_lista_nivel(declaaraciones.com.piso))
    pintar_pantalla.actualizar_pantalla(declaaraciones.com, ene, declaaraciones.J, f" Inicio de cmbate")
    while declaaraciones.J.vida_act > 0 and ene.vida_act > 0:
        acion = indicar_acion.preguntar_acion(declaaraciones.com.aciones)
        if acion == 0:
            declaaraciones.J.atacar(ene)
            pintar_pantalla.actualizar_pantalla(declaaraciones.com, ene, declaaraciones.J,
                                                f" Inflingistes {declaaraciones.J.ataque - ene.defensa} de daño ")
            ene.atacar(declaaraciones.J)
            pintar_pantalla.actualizar_pantalla(declaaraciones.com, ene, declaaraciones.J,
                                                f" Te hicieron {ene.ataque - declaaraciones.J.defensa} de daño ")
    pintar_pantalla.actualizar_pantalla(declaaraciones.final, ene, declaaraciones.J,
                                        f" final combate, llendo al hub ")
    ene.vida_act = ene.vida_max
    selecionar()


def comprar():
    pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, "Bienvenido al balulaque")
    acion = indicar_acion.preguntar_acion(declaaraciones.tienda.aciones)
    if acion == 0:
        pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, "¿Que desea comprar?")
        item = indicar_acion.preguntar_acion(productos, "Introduce ID del producto")
        declaaraciones.J.mochila.append(productos[item])
        pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, f"Compraste {productos[item].nombre}")
        input("Enter para salir: ")
        comprar()
    if acion == 2:
        selecionar()


def selecionar():
    pintar_pantalla.actualizar_pantalla(declaaraciones.Hub, None, None, None)
    acion = indicar_acion.preguntar_acion(declaaraciones.Hub.aciones)
    if acion == 0:
        comprar()
    if acion == 1:
        combate()


combate()
