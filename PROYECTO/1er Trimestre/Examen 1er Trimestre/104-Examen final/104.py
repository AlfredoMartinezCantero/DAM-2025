#Preguntas específicas del examen

#Conecta los ejercicios realizados en programación, marcas y bases de datos

#Sobre la máquina virtual, asegúrate de tener la base de datos en funcionamiento

#Crea un archivo de python que use flask

#Utiliza flask para construir una página HTML/CSS dinámica en base al contenido de la base de datos MySQL

#La web se puede construir encadenando cadenas, no es necesario usar render_template en este trimestre

import mysql.connector          # Importo el conector a base de datos
from flask import Flask         # Importo 

db = mysql.connector.connect(
    host="localhost",
    user="usuario",  
    password="contraseña",
    database="portafolioexamen "
)

cursor = db.cursor()            # Creo el cursor para hacer consultas
app = Flask(__name__)            # Creo la aplicación Flask

@app.route("/")                  # Defino el endpoint principal
def holamundo():
    cursor.execute("SELECT * FROM vista_portafolio")  # Ejecuto la consulta        
    filas = cursor.fetchall()      # Guardo el resultado en una lista

########## AQUI PONGO EL INICIO HASTA EL MAIN 
    cadena = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width", initial-scale="1.0">
    <title>Portafolio examen</title>
    <style>
        body {
            font-family: Arial, san-serif;
            margin: 0;
            padding: 0;
            background-color: #676262;
        }
        header, footer {
            background-color: #27ace6;
            color: rgb(255,255,255);
            text-align: center;
            padding: 1em 0;
        }
        main {
            display: grid;
            grid-template-columns: auto auto auto;
            padding: 20px;
        }
        article {
            background-color: rgb(255,255,255);
            margin-bottom: 20px;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1)
        }
        article img {
            max-width: 40%;
            height: auto;
        }
        h2{
            color: #000000;
        }
    </style>
</head>
<body>
    <header>
        <h1>Piezas portafolio</h1>
        <p>Email: alfredomartinezcantero@gmail.com</p>
    </header>
    <main>
    '''                 # Creo una cadena vacia

############ AQUI PONGO EL BUCLE QUE SE REPITE
    for fila in filas:                           
        cadena +='''
        <article>
            <h2>La noche estrellada</h2>
            <p>Pintado en junio de 1889</p>
            <img src="https://m.media-amazon.com/images/I/71goHUmfvqL.jpg">
            <p>Categoría: <strong>RPG</strong></p>
            <p><strong>Descripción:</strong> Pintura de Vincent van Gogh que representa un cielo nocturno turbulento con estrellas brillantes, remolinos y una luna creciente, contrastando con un pueblo tranquilo en la base del lienzo.</p>
            <p><a href="https://historia-arte.com/obras/noche-estrellada-van-gogh">Ver más</a></p>
        </article>
        '''

############ AQUI PONGO EL FINAL
    cadena += '''
    </main>
<footer>
    <p>&copy; 2025 Alfredo Martínez Cantero</p>
</footer>
</body>
</html>
    '''
    return cadena                          # Devuelvo la cadena como HTML en la web

if __name__ == "__main__":                # Si este es el archivo principal
    app.run(debug=True)                   # Ejecuta la web
