def preguntar_acion(aciones):
    acion = int(input("Introduce el numero coresponiente a la ación: "))
    a_indice_lista = acion - 1
    return int(a_indice_lista)  # devuelve la posicion en lista de la acion selecionada
