print("Catálogo de películas v0.1")
import json     # Para usar la libreria tengo que importarla

catalogo_peliculas = []

while True:
    print("Selecciona una opción")
    print("1.-Añadir una película al catálogo")
    print("2.-Ver catálogo completo")
    print("")
    opcion = int(input("Tu opción: "))

    if opcion == 1:
        print("Añadimos una película al catálogo: ")
        nombre = input("Indica el nombre de la película: ")
        año = input("Indica el año de estreno de la película: ")
        catalogo_peliculas.append({"titulo":nombre,"año":año})
        print("")
        archivo = open("catalogo.json","w")           # Abro un archivo
        json.dump(catalogo_peliculas,archivo)      # Guardo en JSON
        archivo.close()                            # Cierro el archivo

    elif opcion == 2:
        print("Listamos las películas del catálogo: ")
        print(catalogo_peliculas)
        for pelicula in catalogo_peliculas:
            print("Título:",pelicula["titulo"])
            print("Año:",pelicula["año"])
            print("##############################")     # Esto es estético, un separador