archivo = open(r"C:\Users\alfre\Documents\GitHub\DAM-2025\PROGRAMACION\2º Trimestre\TEMA 6-Aplicación de las estructuras de almacenamiento\005-Cadenas de caracteres\001-Las strings realmente son colecciones\007-Leer archivo csv\clientes.csv", "r")

lineas = archivo.readlines()

for linea in lineas:
    partido = linea.split(",")
    print(partido)