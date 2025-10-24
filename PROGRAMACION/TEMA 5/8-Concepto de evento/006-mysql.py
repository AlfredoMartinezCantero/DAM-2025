import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Accesoadatos2526$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
  INSERT INTO clientes
  VALUES(
    1,
    "12345678Z"
    "Alfredo",
    "Martínez Cantero",
    "alfredomartinezcantero@gmail.com"
  );
''')

conexion.commit()

cursor.close()
conexion.close()
