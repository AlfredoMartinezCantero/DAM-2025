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
# ---------------------- ESTO ENVÍA LAS TABLAS ------------------------------------------------------- #
cursor.execute("SHOW TABLES;")          # Muestra las tablas de la base de datos
tablas = []                             # Creo una lista vacia
filas = cursor.fetchall()               # Lo guardo en una lista
for fila in filas:                      # Recorro el resultado
    tablas.append(fila[0])              # Lo añado a la lista de tablas
# ---------------------- ESTO ENVÍA LAS CABECERAS DE LAS TABLAS -------------------------------------- #
cursor.execute("SHOW COLUMNS in Piezas;")          
columnas = []                             
filas = cursor.fetchall()               
for fila in filas:                      
    columnas.append(fila[0])
# ---------------------- ESTO ENVÍA TODA LA TABLA ---------------------------------------------------- #
cursor.execute("SELECT * FROM Piezas;")          
contenido_tabla = cursor.fetchall()                             
######################################### MYSQL ##########################################################

app = Flask(__name__)

@app.route("/")                 
def inicio():   
    return render_template(
        "backoffice.html",
        mis_tablas = tablas,
        mis_columnas = columnas,
        mi_contenido_tabla = contenido_tabla
        )                        # Envío las tablas a HTML

if __name__ == "__main__":
    app.run(debug=True)