# pedir edad ##########################################################
edad_mago = input("Introduce la edad del mago: ")
# convertir a entero ##########################################################
try:
    edad_mago = int(edad_mago)
except:
# si falla, por 100 ##########################################################
    edad_mago = 100
# clasifica por edad ##########################################################
if edad_mago < 30
    clasificacion_mago = "Aprendiz"

# menor que 30 es Aprendiz
# de 30 a 99 es Hechicero
# mas de 100 es Archimago

# funcion poderBase, recibe edad, devuelve entero ########################
# si es Aprendiz, devuelve 5
# si es Hechicero, devuelve 8
# si es Archimago, devuelve 10

# empezamos bucle ##########################################################
# escudo empieza con 15 puntos
# recorre dos turnos con for
# turno 1 fuego daños = poderBase // 2
# turno 2 hechizo rayo = daño = poderBase // 3
# resta el daño al escudo
# si energia escudo baja de cero, ajusta a cero

# tras cada daño, print de daño y mayor que cero ###########################
# tras ajuste energia, print y energia es mayor que cero

# salida: edad, rango, poder base, energia del escudo ###########################
# energia es cero, mago rompe escudo
# energia mayor que cero, escudo resiste duelo

