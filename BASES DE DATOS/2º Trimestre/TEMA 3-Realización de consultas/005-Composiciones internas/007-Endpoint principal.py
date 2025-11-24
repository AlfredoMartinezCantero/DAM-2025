import mysql.connector 
from flask import Flask, render_template, jsonify, g

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host="localhost",
            user="tiendaclase",
            password="Tiendaclase123$",
            database="tienda"
        )
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route("/")
def raiz():
    return render_template("index.html")

# http://127.0.0.1:5000/clientes
@app.route("/clientes")
def clientes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clientes;")
    filas = cursor.fetchall()
    cursor.close()
    return jsonify(filas)

# http://127.0.0.1:5000/tablas
@app.route("/tablas")
def tablas():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SHOW TABLES;")
    filas = cursor.fetchall()
    cursor.close()

    tablas = [fila[0] for fila in filas]
    return jsonify(tablas)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)  # ver punto 2
