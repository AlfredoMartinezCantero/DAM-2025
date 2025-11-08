import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

suma = 0
contador_archivos = 0

for elemento in elementos:
    ruta = os.path.join(carpeta,elemento)
    if os.path.isfile(ruta):
        suma += os.path.getsize(ruta)
        contador_archivos += 1

print("La carpeta ocupa:")
print(suma/(1024*1024),"MB")
print("Número de archivos:", contador_archivos)