#Paso 1: Introducir un nuevo contacto
def nuevo_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    email = input("Introduce el email del contacto: ")

    archivo = open('agenda.txt', 'a')
    archivo.write(nombre + "," + email + "\n")
    archivo.close()

#Paso 2: Leer todos los contactos
def leer_contactos():
    archivo = open('agenda.txt', 'r')
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas:
        partes = linea.strip().split(",")
        if len(partes) == 2:
            nombre, email = partes
            print("Nombre: " + nombre)
            print("Email: " + email)
            print("----")

#Paso 3: Interfaz de usuario
print("Menú:")
print("1.- Introducir un nuevo contacto")
print("2.- Leer todos los contactos")
opcion = input("Selecciona una opción: ")

if opcion == "1":
    nuevo_contacto()
elif opcion == "2":
    leer_contactos()
else:
    print("Opción no válida.")