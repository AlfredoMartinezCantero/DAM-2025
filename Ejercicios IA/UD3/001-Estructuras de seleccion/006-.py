edad_musical = input("Introduce tu edad: ")
edad_musical = int(edad_musical)

if edad_musical < 10:
    mensaje = "Eres un niño."
elif edad_musical >= 10 and edad_musical < 20:  
    mensaje = "Eres un adolescente."
elif edad_musical >= 20 and edad_musical < 30:  
    mensaje = "Eres un joven."
else:            
    mensaje = "Ya no eres un joven."

print(mensaje)


