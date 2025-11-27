import random

patron = {1,2,3,4,5,6,7,8,9}

while True:
    lista = []
    for i in range(1,10):
        lista.append(random.randint(1,9))
    conjunto = set(lista)
    if conjunto == patron:
        print("El conjunto cumple con el patrón")
        print(conjunto)
        print(lista)
        # Ahora elimino un número
        indice = random.randint(1,9)
        lista[indice] = "_" # Escoge un índice(numero) al azar y reemplaza su valor
        print(lista)
        break   # Fuerza la finalidad del bucle infinito


