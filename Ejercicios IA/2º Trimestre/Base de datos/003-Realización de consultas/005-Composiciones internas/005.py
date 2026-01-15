from flask import Flask, jsonify
import mysql.connector
import json

app = Flask(__name__)

# Configuración de la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",        
    password="tiendaclase123$",        
    database="tiendaclase"
)

@app.route("/")
def inicio():
    return "API de Tienda Clase funcionando"

@app.route("/clientes")
def clientes():
    cursor = conexion.cursor(dictionary=True) # dictionary=True nos devuelve objetos JSON directos
    cursor.execute("SELECT * FROM clientes")
    filas = cursor.fetchall()
    cursor.close()
    return jsonify(filas)

@app.route("/tablas")
def tablas():
    # Creamos el cursor para ejecutar la consulta
    cursor = conexion.cursor() 
    cursor.execute("SHOW TABLES;")  
    
    filas = cursor.fetchall()
    
    # Procesamos la tupla que devuelve MySQL para dejar solo una lista de nombres
    lista_tablas = []
    for fila in filas:
        lista_tablas.append(fila[0])
    
    # Cerramos el cursor para liberar recursos
    cursor.close()
    
    # Devolvemos la lista en formato JSON
    return jsonify(lista_tablas)

if __name__ == "__main__":
    app.run(debug=True)