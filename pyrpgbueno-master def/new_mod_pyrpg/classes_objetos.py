import classes_entidades

class Item():
    def __init__(self, suma):
        self.suma=suma
class Pocion(Item):
    def __init__(self, suma):
        super().__init__(suma)
    def usar (self, entidad):
        entidad.vida_act += self.suma
class Escudo (Item):
    def __init__(self, suma):
        super().__init__(suma)
    def usar (self, entidad):
        if type(entidad)==classes_entidades.Jugador:
            entidad.escudo_act += self.suma
        else:
            raise TypeError("Esta entidad no tiene la carasteristica 'escudo'")


