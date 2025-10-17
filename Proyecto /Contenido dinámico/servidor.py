from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
################################ ESTO ES UN BLOQUE
    cadena = '''
    <!doctype html>
<html lang="es">
  <head>
    <title>ALFREDO's blog</title>
    <meta charset="utf-8">
    <style>
      body{background:steelblue;color:steelblue;font-family:sans-serif;}
      header,main,footer{background:white;padding:20px;margin:auto;width:600px;}
      header,footer{text-align:center;}
      main{color:black;}
    </style>
  </head>
  <body>
    <header><h1>ALFREDO's blog</h1></header>
    <main>
    '''
########################## ESTO ES OTRO BLOQUE
    archivo = open("blog.json",'r')
    contenido = json.load(archivo)
    for linea in contenido:
        cadena += '''
          <article>
            <h3>'''+linea['título']+'''</h3>
            <time>'''+linea['fecha']+'''</time>
            <p>'''+linea['autor']+'''</p>
            <p>'''+linea['contenido']+'''</p>
          </article>
          '''
################################### ESTO ES OTRO BLOQUE
    cadena += '''
        </main>
        <footer>(c) 2025 Alfredo Martínez Cantero</footer>
      </body>
    </html>
    '''
############################# No os olvidéis de RETURN
    return cadena

if __name__ == "__main__":
    aplicacion.run(debug=True) 

