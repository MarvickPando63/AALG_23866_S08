import random

def suma_multiplos(lista, indice=0):
    # Caso base: si llegamos al final de la lista
    if indice == len(lista):
        return 0
    # Si el número actual es múltiplo de 3, lo sumamos
    if lista[indice] % 3 == 0:
        return lista[indice] + suma_multiplos(lista, indice + 1)
    else:
        return suma_multiplos(lista, indice + 1)

def main():
    n = int(input("Ingrese la cantidad de elementos: "))
    lista = [random.randint(10, 99) for _ in range(n)]
    print("Lista generada:", lista)

    resultado = suma_multiplos(lista)
    print("Suma de múltiplos de 3:", resultado)

if __name__ == "__main__":
    main()
