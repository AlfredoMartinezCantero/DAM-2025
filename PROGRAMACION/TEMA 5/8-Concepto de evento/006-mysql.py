# pip3 install mysql-connector-python
# sudo apt install libmysqlclient-dev python3-mysql.connector
# solo si da error de ssl en socket:
# pip3 install --user --upgrade mysql-connector-python --break-system-packages
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
