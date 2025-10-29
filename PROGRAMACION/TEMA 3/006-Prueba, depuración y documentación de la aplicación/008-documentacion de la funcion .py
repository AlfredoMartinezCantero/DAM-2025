def hazDivision(dividendo,divisor):
'''
    Función de división
    Entradas: dividendo y divisor que se espera que sean numéricos
    Salidas: resultado de la división como número (o cero si hay fallo)
    Capturas de error:
    1.-Si es numérico
    2.-Si se puede convertir a número
    3.-Si no es división entre cero
'''

    print("Entramos en la función")
    if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
    print("Parece que los parámetros son números")
    if divisor != 0:
        print("Parece que los puedo dividir")
        resultado = dividendo/divisor
        return resultado
    else:
        print("No puedo dividir por que el divisor es cero")
        resultado = 0
    else:
        print("Los parámetros no son números, pero voy a intentar convertirlos")
        try:
        print("Intento convertir a números con éxito")
        dividendo = float(dividendo)
        divisor = float(divisor)
        resultado = dividendo/divisor
        return resultado
    except:
        print("He intentado convertir a números, pero no he podido")
        return 0
print(hazDivision(4,"3"))


