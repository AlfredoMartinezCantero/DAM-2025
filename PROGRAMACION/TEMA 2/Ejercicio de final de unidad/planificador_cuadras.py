#En este ejercicio, se solicita al usuario que ingrese el número de caballos y la capacidad por cuadra para calcular cuántas cuadras son necesarias. Además, se pide una fecha y se determina si esa fecha cae en fin de semana o entre semana.
#Sirve para planificar la infraestructura necesaria para alojar caballos y para identificar la naturaleza de una fecha específica.
#Se utilizan conceptos de entrada de datos, cálculos matemáticos (redondeo al alza) y manipulación de fechas en Python.
#El programa primero solicita al usuario que ingrese el número de caballos y la capacidad por cuadra, asegurándose de que ambos sean enteros positivos. Luego, calcula el número de cuadras necesarias utilizando la función `math.ceil` para redondear al alza. Después, solicita una fecha (año, mes, día) y verifica si es válida. Finalmente, determina si la fecha cae en fin de semana o entre semana utilizando el método `isoweekday()`.
#El funcionamiento paso a paso es el siguiente:
#1. Importar los módulos necesarios (`date` de `datetime` y `math`).
#2. Solicitar al usuario el número de caballos y la capacidad por cuadra, validando que sean enteros positivos.
#3. Calcular el número de cuadras necesarias usando `math.ceil`.
#4. Solicitar al usuario una fecha (año, mes, día) y validar su validez.
#5. Imprimir un informe con los datos ingresados y calculados.
#Errores comunes incluyen ingresar valores no enteros o negativos para el número de caballos o la capacidad por cuadra, así como ingresar fechas inválidas. Estos errores se manejan mediante bloques `try-except` para asegurar que el programa no falle y proporcione mensajes de error claros al usuario.

from datetime import date
import math

try:
    caballos = int(input("Ingrese el número de caballos (entero > 0): "))
    if caballos <= 0:
        print("Error: El número de caballos debe ser un entero positivo.")
        exit()

except:
    print("Error: Entrada no válida para el número de caballos.")
    exit()

try:
    capacidad_por_cuadra = int(input("Ingrese la capacidad por cuadra (entero > 0): "))
    if capacidad_por_cuadra <= 0:
        print("Error: El número debe ser mayor que 0.")
        exit()
except:
    print("Error: Debe ingresar un número entero válido")
    exit()
try:
    anio = int(input("Ingrese el año: "))
    mes = int(input("Ingrese el mes: "))
    dia = int(input("Ingrese el día: "))
    fecha = date(anio, mes, dia)
except:
    print("Error: los valores de la fecha no son válidos.")
    exit()

cuadras_necesarias = math.ceil(caballos / capacidad_por_cuadra)

print("")
print("=== INFORME DE PLANIFICACIÓN DE CUADRAS ===")
print("Caballos:", caballos)
print("Capacidad por cuadra:", capacidad_por_cuadra)
print("Cuadras necesarias (redondeadas al alza):", cuadras_necesarias)
print("")

print("")
print("=== DATOS DE LA FECHA ===")
print("Fecha:", fecha)
print("Año:", anio)
print("Mes:", mes)
print("Día:", dia)
print("")


if fecha.isoweekday() >= 6:
    print("La fecha cae en fin de semana.")
else:
    print("La fecha cae entre semana.")