import mysql.connector
import matplotlib.pyplot as plt

# Configuración de la conexión
db_config = {
    "host": "localhost",
    "user": "clientes",
    "password": "Clientes123$",
    "database": "clientes_ejercicio"
}

try:
    # Establecimiento de conexión y cursor
    conexion = mysql.connector.connect(**db_config)
    cursor = conexion.cursor()

    # Ejecución de consultas de redondeo
    consultas = {
        'ROUND': "SELECT ROUND(AVG(edad)) FROM clientes;",
        'FLOOR': "SELECT FLOOR(AVG(edad)) FROM clientes;",
        'CEIL':  "SELECT CEIL(AVG(edad)) FROM clientes;"
    }
    
    resultados_valores = []
    resultados_labels = []

    for tipo, query in consultas.items():
        cursor.execute(query)
        valor = cursor.fetchone()[0] # Recuperamos el dato único
        resultados_valores.append(valor)
        resultados_labels.append(f"{tipo} ({valor})")
        print(f" - {tipo}: {valor}")

    # Identificación del cliente más joven
    cursor.execute("SELECT nombre, apellidos, edad FROM clientes ORDER BY edad ASC LIMIT 1;")
    joven = cursor.fetchone()
    if joven:
        print(f"\nEl cliente más joven es {joven[0]} {joven[1]} con {joven[2]} años.")

    # Visualización de datos
    plt.figure(figsize=(6, 6))
    plt.pie(resultados_valores, labels=resultados_labels, autopct='%1.1f%%', startangle=140)
    plt.title(f"Redondeo de Edad Promedio\n(Cliente más joven: {joven[0]})")
    plt.axis('equal') 
    plt.show()

except mysql.connector.Error as err:
    print(f"Error en la base de datos: {err}")
except Exception as e:
    print(f"Error general: {e}")

