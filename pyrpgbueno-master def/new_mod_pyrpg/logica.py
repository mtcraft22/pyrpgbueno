import random



import declaaraciones
import lista_enemigos_por_nivel
import pintar_pantalla
import indicar_acion


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
    pintar_pantalla.actualizar_pantalla(declaaraciones.tienda, None, declaaraciones.J, "Apu: bienvenido al balulaque")
    acion = indicar_acion.preguntar_acion(declaaraciones.tienda.aciones)
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
