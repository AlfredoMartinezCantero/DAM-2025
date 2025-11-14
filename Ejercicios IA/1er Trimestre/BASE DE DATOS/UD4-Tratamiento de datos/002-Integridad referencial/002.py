import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="usuarioempresarial",
    password="usuarioempresarial",
    database="empresarial"
)

cursor = conexion.cursor()

while True:
    print("-------------------------------")
    print("GESTIÓN DE CLIENTES")
    print("-------------------------------")
    print("1.- Insertar un cliente")
    print("2.- Listar los clientes")
    print("3.- Actualizar un cliente")
    print("4.- Borrar un cliente")
    print("5.- Salir")

    try:
        opcion = int(input("Escoge tu opción: "))
    except ValueError:
        print("Debes introducir un número.")
        continue

    if opcion == 1:
        print("--- Insertamos un cliente ---")
        nombre = input("Introduce el nombre del cliente: ")
        apellidos = input("Introduce los apellidos del cliente: ")
        telefono = input("Introduce el teléfono del cliente: ")
        email = input("Introduce el email del cliente: ")
        localidad = input("Introduce la localidad del cliente: ")

        cursor.execute('''
            INSERT INTO clientes (Nombre, Apellidos, Telefono, Email, Localidad)
            VALUES (%s, %s, %s, %s, %s)
        ''', (nombre, apellidos, telefono, email, localidad))
        conexion.commit()
        print("Cliente insertado correctamente.")

    elif opcion == 2:
        print("--- Listamos los clientes ---")
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()
        for fila in resultados:
            print("ID:", fila[0], "| Nombre:", fila[1], "| Apellidos:", fila[2], "| Teléfono:", fila[3], "| Email:", fila[4], "| Localidad:", fila[5])

    elif opcion == 3:
        print("--- Actualizamos un cliente ---")
        id = input("Introduce el ID del cliente que quieres actualizar: ")

        print("¿Qué dato quieres modificar?")
        print("1.- Teléfono")
        print("2.- Email")
        print("3.- Localidad")

        try:
            campo = int(input("Escoge una opción: "))
        except ValueError:
            print("Opción no válida.")
            continue

        if campo == 1:
            nuevo_valor = input("Introduce el nuevo teléfono: ")
            cursor.execute('''
                UPDATE clientes SET Telefono = %s WHERE Identificador = %s
            ''', (nuevo_valor, id))
        elif campo == 2:
            nuevo_valor = input("Introduce el nuevo email: ")
            cursor.execute('''
                UPDATE clientes SET Email = %s WHERE Identificador = %s
            ''', (nuevo_valor, id))
        elif campo == 3:
            nuevo_valor = input("Introduce la nueva localidad: ")
            cursor.execute('''
                UPDATE clientes SET Localidad = %s WHERE Identificador = %s
            ''', (nuevo_valor, id))
        else:
            print("Opción no válida.")
            continue

        conexion.commit()
        print("Cliente actualizado correctamente.")

    elif opcion == 4:
        print("--- Eliminamos un cliente ---")
        id = input("Introduce el ID del cliente que quieres eliminar: ")

        confirmar = input("¿Seguro que deseas eliminar este cliente? (s/n): ")
        if confirmar.lower() == 's':
            cursor.execute('''
                DELETE FROM clientes WHERE Identificador = %s
            ''', (id,))
            conexion.commit()
            print("Cliente eliminado correctamente.")
        else:
            print("Operación cancelada.")

    elif opcion == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")

cursor.close()
conexion.close()

