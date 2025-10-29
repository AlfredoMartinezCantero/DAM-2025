def hazDivision(dividendo,divisor):

    if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
    if divisor != 0:
        resultado = dividendo/divisor
        return resultado
    else:
        resultado = 0
    else:
        try:
        dividendo = float(dividendo)
        divisor = float(divisor)
        resultado = dividendo/divisor
        return resultado
    except:
        return 0
print(hazDivision(4,"3"))


