import declaaraciones


def sacar_lista_nivel(nivel):
    listxnil = []
    for i in declaaraciones.enemigos_lista:
        if i.planta_minima == nivel:
            listxnil.append(i.nombre)
        else:
            continue
    return listxnil


print(sacar_lista_nivel(100))
