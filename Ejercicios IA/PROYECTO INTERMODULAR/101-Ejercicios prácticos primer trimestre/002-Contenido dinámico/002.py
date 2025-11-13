from flask import Flask
import json

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
    cadena = '''
    <!doctype html>
<html lang="es">
  <head>
    <title>Blog personal</title>
    <meta charset="utf-8">
    <style>
      body{background:#f5f0ff;color:#2b193d;font-family:sans-serif;}
      header,main,footer{background:#ffffff;padding:20px;margin:auto;width:600px;}
      header,footer{text-align:center;background:#e3d9ff;}
      main{color:#3d2b5e;}
    </style>
  </head>
  <body>
    <header><h1>Blog de Alfredo</h1></header>
    <main>
    '''
    with open("blog.json", "r", encoding="utf-8") as archivo:
        contenido = json.load(archivo)
    for linea in contenido:
        cadena += f'''
      <article>
        <h3>{linea['titulo']}</h3>
        <time>{linea['fecha']}</time>
        <p>{linea['autor']}</p>
        <p>{linea['contenido']}</p>
      </article>
      '''
    cadena += '''
    </main>
    <footer>(c)2025 Alfredo Martínez Cantero</footer>
  </body>
</html>
    '''
    return cadena

if __name__ == "__main__":
    aplicacion.run(debug=True)