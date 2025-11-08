def raizSegura(numero):
    import math
    try:
        if not isinstance(numero,(int,float)):
            numero = float(numero)
        elif numero <= 0:     # Solo si es negativo
            return 0
        return math.sqrt(numero)
    except (ValueError, TypeError):
        return "Error, no válido"
# Pruebas de la función
print(raizSegura(16))       # Debería devolver 4.0
print(raizSegura(-4))       # Debería devolver 0
print(raizSegura(0))        # Debería devolver 0
print(raizSegura("9"))      # Debería devolver 3
print(raizSegura("hola"))   # Error no válido