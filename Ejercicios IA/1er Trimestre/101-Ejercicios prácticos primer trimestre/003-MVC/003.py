from flask import Flask, render_template_string
import json

app = Flask(__name__)

data_json = """
{
  "datos personales": {
    "nombre": "Alfredo",
    "apellidos": "Martínez Cantero",
    "email": "alfredomartinezcantero@gmail.com",
    "telefono": "653358447",
    "direccion": "Mi calle",
    "codigopostal": "46022 Valencia"
  },
  "experiencia": "",
  "formación": ""
}
"""

# Convertimos el texto JSON a un diccionario Python
data = json.loads(data_json)
dp = data["datos personales"]

html_template = """
<!doctype html>
<html lang="es">
  <head>
    <title>Curriculum</title>
    <meta charset="utf-8">
    <style>
      html{background:MediumSlateBlue;font-family:sans-serif;}
      body{background:white;margin:auto;min-height:200px;display:flex;width:600px}
      #izquierda{flex:1;background:white;padding:20px}
      #derecha{flex:4;background:white;padding:20px}
    </style>
  </head>
  <body>
    <div id="izquierda"></div>
    <div id="derecha">
      <h1>{{nombre}} {{apellidos}}</h1>
      <p>{{email}}</p>
      <ul>
        <li>{{telefono}}</li>
        <li>{{direccion}}</li>
        <li>{{codigopostal}}</li>
      </ul>
    </div>
  </body>
</html>
"""

@app.route("/")
def cv():
    return render_template_string(html_template, **dp)

if __name__ == "__main__":
    print("Servidor Flask ejecutándose en http://127.0.0.1:5000/")
    app.run(debug=True)