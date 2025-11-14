print("Lista de la compra v0.1")

lista_de_la_compra = []

while True:
    print("Selecciona una opción")
    print("1.-Añadir elemento a la lista")
    print("2.-Leer la lista")
    print("")
    opcion = int(input("Tu opción: "))

    if opcion == 1:
        print("Añadimos un elemento a la lista: ")
        nombre = input("Indica el nombre del producto: ")
        cantidad = input("Indica la cantidad del producto: ")
        lista_de_la_compra.append({"nombre":nombre,"cantidad":cantidad})
        print("")
    elif opcion == 2:
        print("Listamos los elementos de la lista: ")
        print(lista_de_la_compra)
        for producto in lista_de_la_compra:
            print("Producto:",producto["nombre"])
            print("Cantidad:",producto["cantidad"])
            print("##############################")     # Esto es estético, un separador