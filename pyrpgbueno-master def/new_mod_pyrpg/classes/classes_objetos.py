import classes.classes_entidades


class Item:
    def __init__(self, suma, coste, nombre):
        self.suma = suma
        self.coste = coste
        self.nombre = nombre


class Poción(Item):
    def __init__(self, suma, coste, nombre):
        super().__init__(suma, coste, nombre)

    def usar(self, entidad):
        entidad.vida_act += self.suma


class Escudo(Item):
    def __init__(self, suma, coste, nombre):
        super().__init__(suma, coste, nombre)

    def usar(self, entidad):
        if type(entidad) == classes.classes_entidades.Jugador:
            entidad.escudo_act += self.suma
        else:
            raise TypeError("Esta entidad no tiene la carasteristica 'escudo'")
