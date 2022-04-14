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

    def cambio_estado(self, destino, estado):
        destino.estado = estado


class Jugador(Entidades):
    def __init__(self, escudo, nombre, ataque, defensa, vida):
        super().__init__(nombre, ataque, defensa, vida)
        self.escudo_max = escudo
        self.escudo_act = escudo
        self.dinero = 0


class Enemigos(Entidades):
    def __init__(self, planta, peso, nombre, ataque, defensa, vida):
        super().__init__(nombre, ataque, defensa, vida)
        self.planta_minima = planta
        self.peso = peso


class EnemigosComplejos(Enemigos):
    def __init__(self, planta, peso, transformaciones, nombre, ataque, defensa, vida):
        super().__init__(nombre, planta, peso, ataque, defensa, vida)
        self.transformaciones = transformaciones
