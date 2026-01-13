import mysql.connector
from flask import Flask, render_template

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="composiciones",  
        password="Composiciones123$",
        database="composiciones"
    )

app = Flask(__name__)

@app.route("/")
def inicio():
    conexion = obtener_conexion()
    
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM matriculas_join;")
    filas = cursor.fetchall()
    
    cursor.close()
    conexion.close()
    
    return render_template("index.html", matriculas=filas)   

if __name__ == "__main__":
    app.run(debug=True)