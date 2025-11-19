import pickle
agenda = []

while True:
    # Insertar
    nombre = input("Dime tu nombre: ")
    apellidos = input("Dime tus apellidos: ")
    email = input("Dime tu email: ")
    telefono = input("Dime tu número de teléfono: ")
    agenda.append([nombre,apellidos,email,telefono])
    # Imprimir
    print(agenda)
    # Guardar
    archivo = open("agenda.bin",'wb')
    pickle.dump(agenda,archivo) # Primero se pone lo que quieres exponer y luego donde lo quieres exponer
    archivo.close()