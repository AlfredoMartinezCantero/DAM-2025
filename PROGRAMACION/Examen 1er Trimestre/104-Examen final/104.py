
# Crea un programa en Python que contenga un CRUD con respecto a lo trabajado en el examen de bases de datos 

# -El programa debe dar una bienvenida, y ofrecer las cuatro opciones CRUD en el menu

# (solo necesario piezas de portafolio, no categorías) 

# -Una vez hecho esto, debe entrar en un While True y debe atrapar las opciones con un if-elif 

# -Las opciones serán procesadas contra MySQL usando SELECT, INSERT, UPDATE y DELETE

import mysql.connector

conexion = mysql.connector.connect(
    host="servidor",
    user="nombredeusuario",
    password="contraseña",
    database="portafolioexamen"
)

cursor = conexion.cursor()

while True:
    print("-------------------------------")
    print("GESTIÓN DE PIEZAS")
    print("-------------------------------")
    print("1.- Insertar una pieza")
    print("2.- Listar las piezas")
    print("3.- Actualizar una pieza")
    print("4.- Borrar una pieza")
    print("5.- Salir")

    try:
        opcion = int(input("Escoge tu opción: "))
    except ValueError:
        print("Debes introducir un número.")
        continue

    if opcion == 1:
        print("--- Insertamos una pieza ---")
        Nombre = input("Introduce el Nombre de la pieza: ")
        Autor = input("Introduce el autor de la pieza: ")
        Fecha = input("Introduce la Fecha de la pieza: ")

        cursor.execute('''
            INSERT INTO piezas (Nombre, Autor, Fecha)
            VALUES (%s, %s, %s)
        ''', (Nombre, Autor, Fecha))
        conexion.commit()
        print("Pieza insertada correctamente.")

    elif opcion == 2:
        print("--- Listamos las piezas ---")
        cursor.execute("SELECT * FROM piezas")
        resultados = cursor.fetchall()
        for fila in resultados:
            print("ID:", fila[0], " Nombre:", fila[1], " Autor:", fila[2], " Fecha:", fila[3])

    elif opcion == 3:
        print("--- Actualizamos una pieza ---")
        id = input("Introduce el ID de la pieza que quieres actualizar: ")

        print("¿Qué dato quieres modificar?")
        print("1.- Nombre")
        print("2.- Autor")
        print("3.- Fecha")

        try:
            campo = int(input("Escoge una opción: "))
        except ValueError:
            print("Opción no válida.")
            continue

        if campo == 1:
            nuevo_valor = input("Introduce el nuevo nombre: ")
            cursor.execute('''
                UPDATE piezas SET Nombre = %s WHERE ID = %s
            ''', (nuevo_valor, id))
        elif campo == 2:
            nuevo_valor = input("Introduce el nuevo Autor: ")
            cursor.execute('''
                UPDATE piezas SET Autor = %s WHERE ID = %s
            ''', (nuevo_valor, id))
        elif campo == 3:
            nuevo_valor = input("Introduce la nueva fecha: ")
            cursor.execute('''
                UPDATE piezas SET Fecha = %s WHERE ID = %s
            ''', (nuevo_valor, id))
        else:
            print("Opción no válida.")
            continue

        conexion.commit()
        print("Pieza actualizada correctamente.")

    elif opcion == 4:
        print("--- Eliminamos una pieza ---")
        id = input("Introduce el ID de la pieza que quieres eliminar: ")

        confirmar = input("¿Seguro que deseas eliminar esta pieza? (s/n): ")
        if confirmar.lower() == 's':
            cursor.execute('''
                DELETE FROM piezas WHERE ID = %s
            ''', (id,))
            conexion.commit()
            print("Pieza eliminada correctamente.")
        else:
            print("Operación cancelada.")

    elif opcion == 5:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")

cursor.close()
conexion.close()
