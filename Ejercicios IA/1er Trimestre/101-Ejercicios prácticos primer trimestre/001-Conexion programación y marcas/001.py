#1.- Instalamos flask.
# pip install flask  (windows)
# pip3 install flask --break-system-packages  (linux/macos)

#2.- Ponemos en marcha el servidor.
from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  return "Esto es HTML desde Flask"
  
if __name__ == "__main__":
  aplicacion.run(debug=True)

#3.- Podemos crear HTML más complejo.
from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  return '''
    <!doctype html>
    <html>
      <head>
        <title></title>
        <style>
          h1{color:red;}
        </style>
      </head>
      <body>
        <h1>Esto es HTML a tope de power</h1>
      </body>
    </html>
  '''
  
if __name__ == "__main__":
  aplicacion.run(debug=True)

#4.- HTML dinámico.
from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  cadena = '''
    <!doctype html>
    <html>
      <head>
        <title></title>
        <style>
          h1{color:red;}
        </style>
      </head>
      <body>
        <h1>Esto es HTML a tope de power</h1>
  '''
       
  for dia in range(1,31):
    cadena += '<div>'+str(dia)+'</div>' 
       
  cadena += '''
      </body>
    </html>
  '''
  return cadena
 
if __name__ == "__main__":
  aplicacion.run(debug=True)