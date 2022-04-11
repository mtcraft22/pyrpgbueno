import classes.classes_entidades as entidad
import classes.classes_ecenario as escenarios
import classes.classes_objetos as items


J = entidad.Jugador(0, "por defecto", 2, 1, 20)
goblin = entidad.Enemigos(0, 20, "goblin", 1, 0.5, 10)
goblin_fuerte = entidad.Enemigos(1, 15, "goblin_fuerte", 2, 1, 10)
poción = items.Poción(6, 10, "Poción: Restaura PS")
escudo = items.Escudo(5, 55, "Te añade escudo en el combate")

lista = [poción, escudo]
tienda = escenarios.Tienda(lista)

