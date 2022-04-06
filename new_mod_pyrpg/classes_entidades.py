class Entidades:
    def __init__(self, ataque, defensa, vida, nombre, habilidades=[]):
        self.ataque = ataque
        self.defensa = defensa
        self.vida_maxima = vida
        self.habilidades = habilidades
        self.vida_actual = vida
        self.nombre = nombre
        self.estado = "Normal"

    def atacar(self, destino):
        destino.vida_actual -= (self.ataque + destino.Defensa)


class Jugador(Entidades):
    def __init__(self, escudo, ataque, defensa, vida, nombre, habilidades=[]):
        super().__init__(ataque, defensa, vida, nombre, habilidades)
        self.escudo_max = escudo
        self.escudo_act = escudo


class Enemigo(Entidades):
    def __init__(self, ataque,piso,peso, defensa, vida, nombre, habilidades=[]):
        super().__init__(ataque, defensa, vida, nombre, habilidades)



