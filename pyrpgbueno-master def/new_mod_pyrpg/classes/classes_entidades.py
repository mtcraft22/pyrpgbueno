from prettytable import *


tabla = PrettyTable()
lista_enemigos = []

class Entidades:
    def __init__(self, nombre, ataque, defensa, vida):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida_max = vida
        self.vida_act = vida
        self.habilidades = []
        self.estado = "Normal"

    def atacar(self, destino):
        destino.vida_act -= (self.ataque - destino.defensa)

    '''def cambio_estado(self, destino, estado):
        destino.estado = estado'''


class Jugador(Entidades):
    def __init__(self, escudo, nombre, ataque, defensa, vida):
        super().__init__(nombre, ataque, defensa, vida)
        self.mochila = []
        self.escudo_max = escudo
        self.escudo_act = escudo
        self.dinero = 0
    def mostrar_items(self):
        id = 0
        tabla.clear()
        tabla.field_names = ["id", "Nombre","Puntos de afectación"]
        for i in self.Items_ala_venta:
            id += 1
            tabla.add_row([f"{id}",f"{i.nombre}",f"{i.suma}"])
        print(tabla)


class Enemigos(Entidades):
    def __init__(self, planta, peso, nombre, ataque, defensa, vida, coin_max, coin_min):
        super().__init__(nombre, ataque, defensa, vida)
        self.planta_minima = planta
        self.peso = peso
        self.max_coin= coin_max
        self.min_coin = coin_min
        lista_enemigos.append(self)

class EnemigosComplejos(Enemigos):
    def __init__(self, planta, peso, transformaciones, nombre, ataque, defensa, vida):
        super().__init__(nombre, planta, peso, ataque, defensa, vida)
        self.transformaciones = transformaciones
