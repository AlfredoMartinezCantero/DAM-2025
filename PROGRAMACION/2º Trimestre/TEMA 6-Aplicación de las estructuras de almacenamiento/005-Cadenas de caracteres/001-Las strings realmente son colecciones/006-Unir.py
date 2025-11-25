datos = "uno,dos,tres,cuatro,cinco,seis"

# Primero imprimo la cadena de caracteres
print(datos)
# Ahora la aparto
partido = datos.split(",")
# Imprimo el partido (lista)
print(partido)
# Ahora quiero unirlo todo de nuevo
nueva_cadena = "|".join(partido)
print(nueva_cadena)