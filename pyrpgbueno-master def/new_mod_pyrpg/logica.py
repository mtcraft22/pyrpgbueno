import pintar_pantalla
import declaaraciones
import time


acion = pintar_pantalla.actualizar_pantalla(declaaraciones.com, declaaraciones.goblin, declaaraciones.J, "realizando pruebas")
while declaaraciones.J.vida_act > 0 and declaaraciones.goblin.vida_act > 0:
    if acion == 0:
        declaaraciones.J.atacar(declaaraciones.goblin)
        pintar_pantalla.actualizar_pantalla(declaaraciones.com, declaaraciones.goblin, declaaraciones.J,
        f" Inflingistes {declaaraciones.J.ataque - declaaraciones.goblin.defensa} de daño ")

pintar_pantalla.actualizar_pantalla(declaaraciones.final, declaaraciones.goblin, declaaraciones.J,
                                            f" final combate, llendo al hub ")
time.sleep(3)

pintar_pantalla.actualizar_pantalla(declaaraciones.Hub, None, None, None)
