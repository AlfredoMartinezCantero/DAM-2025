usuarios = []

def crear_usuario(nombre, edad):
    usuario = (nombre, edad)
    usuarios.append(usuario)
    print("Usuario " + nombre + " creado.")

def leer_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for i, usuario in enumerate(usuarios):
            print(str(i + 1) + ". Nombre: " + usuario[0] + ", Edad: " + str(usuario[1]))

def actualizar_usuario(indice, nombre=None, edad=None):
    if 0 <= indice < len(usuarios):
        usuario_actual = usuarios[indice]
        nuevo_nombre = nombre if nombre else usuario_actual[0]
        nueva_edad = edad if edad else usuario_actual[1]
        usuarios[indice] = (nuevo_nombre, nueva_edad)
        print("Usuario en la posición " + str(indice + 1) + " actualizado.")
    else:
        print("Índice de usuario no válido.")

def eliminar_usuario(indice):
    if 0 <= indice < len(usuarios):
        usuario_eliminado = usuarios.pop(indice)
        print("Usuario " + usuario_eliminado[0] + " eliminado.")
    else:
        print("Índice de usuario no válido.")

def menu():
    while True:
        print("\nOpciones:")
        print("1. Crear usuario")
        print("2. Leer usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '1':
            nombre = input("Ingresa el nombre del usuario: ")
            edad = input("Ingresa la edad del usuario: ")
            crear_usuario(nombre, edad)

        elif opcion == '2':
            leer_usuarios()

        elif opcion == '3':
            indice = int(input("Ingresa el número del usuario a actualizar: ")) - 1
            nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
            edad = input("Nueva edad (deja vacío para no cambiar): ")
            actualizar_usuario(indice, nombre if nombre else None, edad if edad else None)

        elif opcion == '4':
            indice = int(input("Ingresa el número del usuario a eliminar: ")) - 1
            eliminar_usuario(indice)

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
