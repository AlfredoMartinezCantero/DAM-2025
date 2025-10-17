archivo = open("mapa.txt","r") # R = read

lineas = archivo.readlines()

for linea in lineas:
    if "json" in linea:
        print("####################################")
        print("Encontrado!: ", linea)





