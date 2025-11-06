import mysql.connector          # Importo el conector a base de datos
from flask import Flask         # Importo 

db = mysql.connector.connect(
    host="localhost",
    user="usuario_portafolio",  
    password="mi_contraseña_segura",
    database="portafolio"
)

cursor = db.cursor()            # Creo el cursor para hacer consultas
app = Flask(__name__)            # Creo la aplicación Flask

@app.route("/")                  # Defino el endpoint principal
def holamundo():
    cursor.execute("SELECT * FROM vista_portafolio")  # Ejecuto la consulta        
    filas = cursor.fetchall()      # Guardo el resultado en una lista
########## AQUI PONGO EL INICIO HASTA EL MAIN 
    cadena = '''
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portafolio de Piezas Creativas</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #676262;
            }
            header, footer {
                background-color: #a71d9b;
                color: rgb(255, 255, 255);
                text-align: center;
                padding: 1em 0;
            }
            main {
                display: grid;
                grid-template-columns: auto auto auto;
                padding: 20px;
            }
            article {
                background-color: rgb(255, 255, 255);
                margin-bottom: 20px;
                padding: 15px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            article img {
                max-width: 40%;
                height: auto;
            }
            h2 {
                color: #000000;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Mi Portafolio de Piezas Creativas</h1>
            <p>Email: alfredomartinezcantero@gmail.com</p>
        </header>
        <main>
    '''                 # Creo una cadena vacia
############ AQUI PONGO EL BUCLE QUE SE REPITE
    for fila in filas:                           # Para cada elemento de la lista
        cadena += f'''
            <article>
                <h2>{fila[1]}</h2>
                <img src="{fila[2]}" alt="{fila[1]}">
                <p>{fila[3]}</p>
            </article>
        '''
############ AQUI PONGO EL FINAL
    cadena += '''
        </main>
        <footer>
            <p>&copy; 2023 Mi Portafolio de Piezas Creativas</p>
        </footer>
    </body>
    </html>
    '''
    return cadena                          # Devuelvo la cadena como HTML en la web

if __name__ == "__main__":                # Si este es el archivo principal
    app.run(debug=True)                   # Ejecuta la web