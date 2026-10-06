def rec_avanza(actual, inicio):
    # Si esto ocurre, no se encontraron multiplos
    if actual <inicio:
        return inicio
    # Si es multiplo de tres, devuelve ese número
    if actual % 3 == 0:
        return actual
    # Si no es multiplo, hay recursion con un número menor
    return rec_avanza(actual -1, inicio)
    
inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el numero final: "))

if inicio > fin:
    print("El recorrido debe ser hacia adelante.")
else:
    resultado = rec_avanza(fin, inicio)
    # Se hace la comprobación de si es mulltiplo
    if resultado % 3 == 0:
        print("El maximo multiplo de 3 es:", resultado)
    else:
        print("No hay multiplos de 3 en el rango.")