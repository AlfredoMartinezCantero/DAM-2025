import pickle
agenda = []

while True:
    print("Selecciona una opción:")
    print("1.-Insertar un registro")
    print("2.-Leer registros")
    print("3.-Guardar registros")
    print("4.-Cargar registros")
    opcion = int(input("Escoge una opción:"))
    if opcion == 1:
    # Insertar
        nombre = input("Dime tu nombre: ")
        apellidos = input("Dime tus apellidos: ")
        email = input("Dime tu email: ")
        telefono = input("Dime tu número de teléfono: ")
        agenda.append([nombre,apellidos,email,telefono])
    elif opcion == 2:
        # Imprimir
        print(agenda)
    elif opcion == 3:
        # Guardar
        archivo = open("agenda.bin",'wb')
        pickle.dump(agenda,archivo) # Primero se pone lo que quieres exponer y luego donde lo quieres exponer
        archivo.close()
    elif opcion == 4:
        archivo = open("agenda.bin",'rb')
        agenda = pickle.load(archivo)         
        archivo.close()