archivo = open("mapa.txt","r") # R = read
busca = input("Introduce el término a buscar: ")

lineas = archivo.readlines()

for linea in lineas:
    if busca in linea:
        print("####################################")
        print("Encontrado!: ",linea)





