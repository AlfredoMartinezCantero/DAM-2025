import random

def genera_cancion():
    #range(1, 10) es como una "baraja" (del 1 al 9)
    #9 es la cantidad de "cartas" que hay que sacar
    return random.sample(range(1, 10), 9)

def es_correcta(cancion):
    #Creo el molde, un conjunto del 1 al 9
    molde = set(range(1, 10))
    
    #Convierto la lista en conjunto (si hay repetidos desaparecen aquí)
    conjunto = set(cancion)
    
    #Si son matemáticamente iguales es True
    return conjunto == molde

def genera_matriz():
    matriz = []
    
    for i in range(10):
        nueva_fila = genera_cancion()
        matriz.append(nueva_fila) #Guardamos la fila
        
    return matriz

canciones = genera_matriz()

print("REVISIÓN DE CANCIONES")
for fila in canciones:
    #Imprimo la lista y el resultado de su validación
    print(f"{fila} -> ¿És válida?: {es_correcta(fila)}")