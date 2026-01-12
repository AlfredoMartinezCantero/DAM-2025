from flask import Flask, render_template, request, jsonify
import sys
import io
import uuid
import os

template_dir = os.path.abspath('../front/templates')
app = Flask(__name__, template_folder=template_dir)

sesiones = {} 

@app.route('/')
def home():
    # Ahora Flask buscará este archivo en la carpeta front/templates
    return render_template('frentemasampliado.html')

@app.route('/api/start')
def start():
    token = str(uuid.uuid4())
    sesiones[token] = "" 
    print(f"--> SESIÓN INICIADA: {token}") 
    return jsonify({"token": token})

@app.route('/api/write', methods=['POST'])
def write():
    datos = request.get_json()
    token = datos.get('token')
    codigo = datos.get('codigo')
    
    if token in sesiones:
        sesiones[token] += codigo + "\n"
        return jsonify({"mensaje": "ok"})
    return jsonify({"mensaje": "error", "causa": "Token invalido"}), 400

@app.route('/api/read', methods=['POST'])
def read():
    datos = request.get_json()
    token = datos.get('token')
    
    if token not in sesiones:
        return jsonify({"salida": "Error: Sesión no encontrada"})

    buffer = io.StringIO()
    sys.stdout = buffer
    
    try:
        exec(sesiones[token])
        resultado = buffer.getvalue()
    except Exception as e:
        resultado = f"Error: {str(e)}"
    finally:
        sys.stdout = sys.__stdout__
    
    return jsonify({"salida": resultado})

if __name__ == '__main__':
    app.run(debug=True, port=5000)