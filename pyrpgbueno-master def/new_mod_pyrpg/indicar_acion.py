def preguntar_acion(aciones, com="Introduce el numero coresponiente a la ación:"):
    acion = int(input(com))
    a_indice_lista = acion - 1
    return int(a_indice_lista)  # devuelve la posicion en lista de la acion selecionada
