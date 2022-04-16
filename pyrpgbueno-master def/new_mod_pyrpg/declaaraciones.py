import classes.classes_entidades as entidad
import classes.classes_ecenario as escenarios
import classes.classes_objetos as items

# declaramos las entidades que combaten

J = entidad.Jugador(0, "por defecto", 2, 1, 20)
goblin = entidad.Enemigos(0, 20, "goblin", 1, 0.5, 10)
goblin_fuerte = entidad.Enemigos(1, 15, "goblin_fuerte", 2, 1, 10)


# declaramos las instancias de los objectos

poción = items.Poción(6, 10, "Poción, restaura PS")
escudo = items.Escudo(5, 55, "Te añade escudo en el combate")

# lista items de la tienda
lista = [poción, escudo]
# lista enemigos
enemigos_lista = [goblin, goblin_fuerte, boss_basico, boss_basico2, boss_basico5, boss_basico4, boss_basico3]
# declaramos los escenarios
Hub = escenarios.Escenarios(nombre="Hub", aciones=["Tienda", "Combate"])
com = escenarios.Combate(nombre="combate", aciones=["atacar", "defender", "objecto", "habilidad"])
tienda = escenarios.Tienda(items=lista, nombre="tienda", aciones=["comprar", "vender", "ir hub"])
final = escenarios.Combate(nombre="final", aciones=[])


