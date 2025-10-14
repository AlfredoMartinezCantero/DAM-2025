def hazDivision(dividendo, divisor):
    print("Entramos en la función")
    
    if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
        print("Parece que los parámetros son números")
        if divisor != 0:
            print("Parece que los puedo dividir")
            resultado = dividendo / divisor
            return resultado
        else:
            print("No puedo dividir porque el divisor es cero")
            return 0
    else:
        print("Los parámetros no son números, pero voy a intentar convertirlos")
        try:
            dividendo = float(dividendo)
            divisor = float(divisor)
            print("Intento convertir a números con éxito")
            if divisor != 0:
                resultado = dividendo / divisor
                return resultado
            else:
                print("No puedo dividir porque el divisor convertido es cero")
                return 0
        except:
            print("He intentado convertir a números, pero no he podido")
            return 0


print(hazDivision(4, "3"))



