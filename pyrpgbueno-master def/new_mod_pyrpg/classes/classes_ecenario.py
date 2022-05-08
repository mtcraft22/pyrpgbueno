from prettytable import *

tabla = PrettyTable()


class Escenarios:
    def __init__(self, nombre, aciones):
        self.nombre = nombre
        self.aciones = aciones


class Combate(Escenarios):
    def __init__(self, nombre, aciones):
        super().__init__(nombre, aciones)
        self.piso = 1


class Tienda(Escenarios):
    def __init__(self, items, nombre, aciones):
        super().__init__(nombre, aciones)
        self.Items_ala_venta = items

    def mostrar_items(self):
        tabla.field_names = ["Nombre", "Coste", "Puntos de curación"]
        for i in self.Items_ala_venta:
            tabla.add_row([f"{i.nombre}", f"{i.coste}", f"{i.suma}"])
        print(tabla)





