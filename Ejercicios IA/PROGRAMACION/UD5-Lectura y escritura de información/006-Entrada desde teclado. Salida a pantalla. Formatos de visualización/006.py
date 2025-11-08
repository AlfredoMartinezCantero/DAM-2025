class Cliente():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        
print("Gestión de clientes v0.1")
print("Por: Alfredo Martínez Cantero")

clientes = []

while True:
    print("")
    print("Escoge una opción:")
    print("")
    print("1.-Insertar un cliente")
    print("")
    print("2.-Listar un cliente")
    print("")
    print("3.-Actualizar un cliente")
    print("")
    print("4.-Eliminar un cliente")
    print("")
    opcion = int(input("Escoge una opción: "))
    print("")
    
    if opcion == 1:
        print("")
        nombre = input("Introduce el nombre: ")
        print("")
        apellidos = input("Introduce los apellidos: ")
        print("")
        email = input("Introduce el email: ")
        print("")
        clientes.append(Cliente(nombre,apellidos,email))
        print("")
    elif opcion == 2:
        identificador = 0
        for cliente in clientes:
            print("")
            print("Este es el cliente con el ID:",identificador)
            print("")
            print(cliente.nombre,cliente.apellidos,cliente.email)
            print("")
            identificador += 1
    elif opcion == 3:
        print("")
        identificador = int(input("Introduce el ID para modificar: "))
        print("")
        nombre = input("Introduce el nombre: ")
        print("")
        apellidos = input("Introduce los apellidos: ")
        print("")
        email = input("Introduce el email: ")
        print("")
        clientes[identificador].nombre = nombre
        print("")
        clientes[identificador].apellidos = apellidos
        print("")
        clientes[identificador].email = email
        print("")
    elif opcion == 4:
        print("")
        identificador = int(input("Introduce el ID para eliminar: "))
        print("")
        confirmacion = input("¿Estás seguro? (S/N): ").lower()
        print("")
        if confirmacion == "s":
            clientes.pop(identificador)
        elif confirmacion == "n":
            print("Cancelado")
        else:
            print("Opción no válida")
            