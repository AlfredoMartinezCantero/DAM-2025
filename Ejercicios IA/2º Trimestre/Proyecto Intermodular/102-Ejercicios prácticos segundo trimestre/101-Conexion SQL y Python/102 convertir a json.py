import mysql.connector 
import json

# Conectar a la base de datos
conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)                                      
  
# Es vital usar dictionary=True para que JSON pueda crear los pares clave:valor
cursor = conexion.cursor(dictionary=True)

cursor.execute('''
  SELECT
    nombre AS "Nombre del cliente",
    apellidos AS "Apellidos del cliente",
    edad AS "Edad del cliente"
  FROM clientes
  ORDER BY edad DESC;
''')  

# Obtener los resultados
filas = cursor.fetchall()

# Serializar la lista de diccionarios a texto JSON
json_result = json.dumps(filas, indent=4, ensure_ascii=False)

print(json_result)

cursor.close()
conexion.close()