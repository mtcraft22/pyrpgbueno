import random
import time

import declaaraciones
import lista_enemigos_por_nivel
import pintar_pantalla


def combate():
    ene = random.choice(lista_enemigos_por_nivel.sacar_lista_nivel(declaaraciones.com.piso))
    acion = pintar_pantalla.actualizar_pantalla(declaaraciones.com, ene, declaaraciones.J, "realizando pruebas")
    while declaaraciones.J.vida_act > 0 and declaaraciones.goblin.vida_act > 0:
        if acion == 0:
            declaaraciones.J.atacar(declaaraciones.goblin)
            pintar_pantalla.actualizar_pantalla(declaaraciones.com, ene, declaaraciones.J,
                                                f" Inflingistes {declaaraciones.J.ataque - declaaraciones.goblin.defensa} de daño ")

    pintar_pantalla.actualizar_pantalla(declaaraciones.final, ene, declaaraciones.J,
                                        f" final combate, llendo al hub ")
    time.sleep(3)

    pintar_pantalla.actualizar_pantalla(declaaraciones.Hub, None, None, None)


combate()
