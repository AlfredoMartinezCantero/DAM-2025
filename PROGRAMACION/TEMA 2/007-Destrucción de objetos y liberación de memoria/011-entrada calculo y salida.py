'''
Calculadora de cuadras
v0.1 (c) 2025 Alfredo Martínez Cantero
Programa que calcula número de cuadras a partir de los caballos
'''

# Datos del inicio
caballos = 0
cuadras = 0


#Entrada de información
caballos = int(input("Intorduce el número de caballos: "))

# Realización de cálculos
cuadras = caballos / 3

# Salida de resultados
print("Si tienes",caballos,"caballos")
print("Y te caben tres caballos por cuadra")
print("En ese caso necesitas",cuadras,"cuadras")
