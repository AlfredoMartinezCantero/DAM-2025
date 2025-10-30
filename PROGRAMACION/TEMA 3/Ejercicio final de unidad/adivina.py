#Este ejercicio consiste en un juego interactivo en Python donde el usuario debe adivinar un número secreto entre 1 y 50. 
#El programa proporciona un máximo de 6 intentos y, después de 3 intentos fallidos, ofrece una pista indicando si el número es par o impar además de ir diciéndonos si es mayor o menos que el que hemos puesto.
#Este tipo de ejercicios son útiles para aprender y practicar conceptos fundamentales de programación, como la generación de números aleatorios, la validación de entradas de usuario, y el uso de estructuras de control `if/elif/else, while` y manejo de errores `try/except`. 
#Se utiliza `assert` para validar que el número secreto y el contador de intentos estén dentro de los rangos esperados.
#Si el usuario adivina el número, se muestra un mensaje de éxito; si no, se revela el número secreto al final.
#Se manejan entradas no válidas para asegurar que el usuario ingrese un número entero dentro del rango especificado.
#El juego termina cuando el usuario adivina el número o agota sus intentos.
#Este programa es útil para practicar lógica de programación, manejo de entradas y salidas, y uso de estructuras de control en Python.
#Un error común es incluir ingresar valores no numéricos o fuera del rango.

import random

secreto = random.randint(1, 50)
intentos = 0
max_intentos = 6

assert 1 <= secreto <= 50, "El número secreto tiene que estar entre el 1 y el 50"
assert intentos >= 0, "El contador de intentos no puede ser negativo"

print("¡Bienvenido/a al juego de adivinar el número secreto!")
print("Tienes", max_intentos, "intentos")

while intentos < max_intentos:
    entrada = input("Introduce un número entre 1 y 50: ")
    
    try:
        numero = int(entrada)
    except:
        print("Entrada no valida. Por favor introduce un número entero.")
        continue

    if numero < 1 or numero > 50:
        print("El número debe estar entre 1 y 50.")
        continue

    intentos += 1

    if numero == secreto:
        print("¡Acertaste! El número secreto era", secreto)
        break
    elif numero < secreto:
        print("Demasiado bajo")
    else:
        print("Demasiado alto")

    if intentos == 3:
        if secreto % 2 == 0:
            print("¡Pista! El número secreto es par.")
        else:
            print("¡Pista! El número secreto es impar.")

if numero != secreto:
    print("Has perdido :(  El número secreto era", secreto)