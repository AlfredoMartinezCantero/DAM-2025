# sudo apt install python3-pip (si no tenemos PIP en Ubuntu)
# pip install flask - Windows
# pip3 install flask --break-system-packages (Linux o macOS / máquina virtual)

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
                h1{color:purple;}
            </style>
        </head>
        <body>
            <h1>Esto es HTML a tope de power</h1>
        </body>
    </html>
'''
    
if __name__ == "__main__":
    aplicacion.run(debug=True) 

