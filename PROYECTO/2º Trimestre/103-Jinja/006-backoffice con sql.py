from flask import Flask, render_template
import mysql.connector

######################################### MYSQL ##########################################################
conexion = mysql.connector.connect(
    host="localhost",
    user="usuario_portafolio",  
    password="mi_contraseña_segura",
    database="portafolio"
)                                       # Datos de conexión a la BBDD
cursor = conexion.cursor()              # Creo un cursor MySQL
cursor.execute("SHOW TABLES;")          # Muestra las tablas de la base de datos
tablas = []                             # Creo una lista vacia
filas = cursor.fetchall()               # Lo guardo en una lista
for fila in filas:                      # Recorro el resultado
    tablas.append(fila[0])              # Lo añado a la lista de tablas
######################################### MYSQL ##########################################################

app = Flask(__name__)

@app.route("/")                 
def inicio():   
    return render_template("backoffice.html",mis_tablas = tablas)

if __name__ == "__main__":
    app.run(debug=True)