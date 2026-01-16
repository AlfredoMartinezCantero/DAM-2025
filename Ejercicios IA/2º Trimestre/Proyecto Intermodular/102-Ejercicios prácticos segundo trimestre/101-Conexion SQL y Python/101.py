import mysql.connector 

# Conectar a la base de datos
conexion = mysql.connector.connect(
  host="localhost",
  user="clientes",
  password="Clientes123$",
  database="clientes"
)                                      
  
# Creamos el cursor en modo diccionario para acceder por nombre de columna
cursor = conexion.cursor(dictionary=True)

# Ejecutamos la consulta proyectando alias y ordenando
cursor.execute('''
  SELECT
    nombre AS "Nombre del cliente",
    apellidos AS "Apellidos del cliente",
    edad AS "Edad del cliente"
  FROM clientes
  ORDER BY edad DESC;
''')  

# Obtener y mostrar los resultados
filas = cursor.fetchall()

print(filas)

cursor.close()
conexion.close()