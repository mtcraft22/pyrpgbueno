from prettytable import *

tabla = PrettyTable()

class Combate:
    def __init__(self):
        self.piso = 1
        self.aciones = ["atacar", "esquivar", "burla"]


class Tienda:
    def __init__(self, items):
        self.Items_ala_venta = items

    def mostrar_items(self):
        tabla.field_names = ["Nombre", "Coste", "suma"]
        for i in self.Items_ala_venta:
            tabla.add_row([f"{i.nombre}", f"{i.coste}", f"{i.suma}"])
        print(tabla)



