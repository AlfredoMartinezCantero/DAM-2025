import mysql.connector

# 1. Conexión a la base de datos con usuario seguro
db = mysql.connector.connect(
    host="localhost",
    user="usuario_portafolio",  # Usuario creado previamente
    password="mi_contraseña_segura",
    database="portafolio"
)

cursor = db.cursor()

# 2. Mensaje de bienvenida
print("===================================")
print("  Bienvenido a tu Portafolio CRUD  ")
print("===================================")

# 3. Bucle principal infinito
while True:
    print("Opciones disponibles:")
    print("1 - Crear nueva pieza")
    print("2 - Ver todas las piezas")
    print("3 - Actualizar una pieza")
    print("4 - Borrar una pieza")
    print("5 - Salir")

    opcion = int(input("Selecciona una opción (1-5): "))

    # 4. Crear nueva pieza
    if opcion == "1":
        titulo = input("Título de la pieza: ")
        descripcion = input("Descripción: ")
        imagen = input("Nombre de la imagen: ")
        url = input("URL: ")
        id_categoria = input("ID de la categoría: ")

        # Insert usando parámetros para seguridad
        sql = "INSERT INTO piezas (titulo, descripcion, imagen, url, id_categoria) VALUES (%s, %s, %s, %s, %s)"
        valores = (titulo, descripcion, imagen, url, id_categoria)
        cursor.execute(sql, valores)
        db.commit()
        print("Pieza creada correctamente.")

    # 5. Ver todas las piezas
    elif opcion == "2":
        sql = """
        SELECT piezas.Identificador, piezas.titulo, piezas.descripcion, piezas.imagen, piezas.url, categorias.titulo
        FROM piezas
        LEFT JOIN categorias ON piezas.id_categoria = categorias.Identificador
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print("--- Lista de piezas ---")
        for fila in resultados:
            print("ID:", fila[0], "| Título:", fila[1], "| Descripción:", fila[2], "| Imagen:", fila[3], "| URL:", fila[4], "| Categoría:", fila[5])

    # 6. Actualizar una pieza
    elif opcion == "3":
        id_pieza = input("Ingresa el ID de la pieza a actualizar: ")
        nuevo_titulo = input("Nuevo título: ")
        nueva_descripcion = input("Nueva descripción: ")
        sql = "UPDATE piezas SET titulo = %s, descripcion = %s WHERE Identificador = %s"
        valores = (nuevo_titulo, nueva_descripcion, id_pieza)
        cursor.execute(sql, valores)
        db.commit()
        print("Pieza actualizada correctamente.")

    # 7. Borrar una pieza
    elif opcion == "4":
        id_pieza = input("Ingresa el ID de la pieza a borrar: ")
        sql = "DELETE FROM piezas WHERE Identificador = %s"
        cursor.execute(sql, (id_pieza,))
        db.commit()
        print("Pieza eliminada correctamente.")

    # 8. Salir de la aplicación
    elif opcion == "5":
        print("Saliendo de la aplicación. ¡Hasta luego!")
        break

    # 9. Opción inválida
    else:
        print("Opción no válida, intenta nuevamente.")

# 10. Cerrar conexión
cursor.close()
db.close()
