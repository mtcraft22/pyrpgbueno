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



class Entidades():
    def __init__(self,nombre,ataque,defensa,vida):
        self.nombre=nombre
        self.ataque=ataque
        self.defensa=defensa
        self.vida_max=vida
        self.vida_act=vida
        self.habilidades=[]
        self.estado="Normal"
    def atacar(self, destino):
        destino.vida_act -= (self.ataque + destino.defensa)
    def cambio_estado(self,destino,estado):
        destino.estado=estado
class Jugador(Entidades):
    def __init__(self,escudo,nombre,ataque,defensa,vida):
        super().__init__(nombre,ataque,defensa,vida)
        self.escudo_max=escudo
        self.escudo_act=escudo
class Enemigos(Entidades):
    def __init__(self,planta,peso,nombre,ataque,defensa,vida):
        super().__init__(nombre,ataque,defensa,vida)
        self.planta_minima=planta
        self.peso=peso
class Enemgos_complejos(Enemigos):
    def __init__(self,planta,peso,transformaciones,nombre,ataque,defensa,vida):
        super().__init__(nombre,planta,peso,ataque,defensa,vida)
        self.transformaciones=transformaciones


J=Enemigos(12,"32",12,12,12,12)

if type(J)==Jugador:
    print("es un jugador")


