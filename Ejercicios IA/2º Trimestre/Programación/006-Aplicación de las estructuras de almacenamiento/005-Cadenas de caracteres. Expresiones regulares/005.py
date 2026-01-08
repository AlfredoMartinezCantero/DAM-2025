#Abrimos el archivo
archivo = open("clientes.csv", "r")

#Leemos el archivo
lineas = archivo.readlines()

#Procesamos las lineas
for linea in lineas:
    #.strip() elimina el enter (\n) del final
    linea_limpia = linea.strip() 
    partido = linea_limpia.split(",")
    print(partido)

archivo.close()