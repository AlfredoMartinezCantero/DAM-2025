import mysql.connector
from flask import Flask

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="usuario_portafolio",
    password="mi_contraseña_segura",
    database="portafolioexamen"
)

@app.route("/")
def mostrar_portafolio():
    cursor = db.cursor()
    cursor.execute("SELECT titulo, descripcion, fecha, categoria FROM vista_piezas_categorias")
    filas = cursor.fetchall()

    cadena = '''
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portafolio de Piezas Creativas</title>
        <style>
            body {font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #676262;}
            header, footer {background-color: #a71d9b; color: white; text-align: center; padding: 1em 0;}
            main {display: grid; grid-template-columns: auto auto auto; padding: 20px;}
            article {background-color: white; margin-bottom: 20px; padding: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
            h2 {color: black;}
        </style>
    </head>
    <body>
        <header>
            <h1>Mi Portafolio de Piezas Creativas</h1>
            <p>Email: alfredomartinezcantero@gmail.com</p>
        </header>
        <main>
    '''

    for titulo, descripcion, fecha, categoria in filas:
        cadena += f'''
        <article>
            <h2>{titulo}</h2>
            <p><strong>Fecha:</strong> {fecha}</p>
            <p><strong>Categoría:</strong> {categoria}</p>
            <p>{descripcion}</p>
        </article>
        '''

    cadena += '''
        </main>
        <footer>
            <p>&copy; 2025 Mi Portafolio de Piezas Creativas</p>
        </footer>
    </body>
    </html>
    '''

    return cadena

if __name__ == "__main__":
    app.run(debug=True)
