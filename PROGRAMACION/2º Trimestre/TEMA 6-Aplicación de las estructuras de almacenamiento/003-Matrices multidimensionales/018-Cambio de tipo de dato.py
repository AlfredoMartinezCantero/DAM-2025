tupla = ('manzanas','peras','platanos')     # Esto es una tupla()
# Necesito meter una fruta más
print(tupla)
lista = list(tupla) # Convierto una tupla en una lista[]
print(lista)
lista.append("fresas")  # Añadimos la fruta que necesitabamos

# Ahora supogamos que tengo que volver a tupla
nueva_tupla = tuple(lista)
print(nueva_tupla)