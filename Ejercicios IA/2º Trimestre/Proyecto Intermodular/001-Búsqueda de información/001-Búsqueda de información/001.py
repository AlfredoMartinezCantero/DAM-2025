from flask import Flask

app = Flask(__name__)

@app.route("/")
def tabla_dinamica():
    # Inicializo la cadena con la estructura básica del HTML y CSS
    cadena = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Calendario Dinámico</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f0f0f0; padding: 20px; }
            table { width: 100%; border-collapse: collapse; background-color: white; }
            th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
            th { background-color: #4CAF50; color: white; }
            tr:nth-child(even) { background-color: #f2f2f2; }
            .dias { color: #555; font-size: 0.9em; }
        </style>
    </head>
    <body>
        <h1>Tabla de 12 Semanas (Días 1-31)</h1>
        <table>
            <thead>
                <tr>
                    <th>Semana / Bloque</th>
                    <th>Días</th>
                </tr>
            </thead>
            <tbody>
    """

    # Genera las 12 filas (Semanas)
    # range(1, 13) genera números del 1 al 12
    for semana in range(1, 13):
        cadena += f"<tr>"
        cadena += f"<td><strong>Semana {semana}</strong></td>"
        cadena += f"<td class='dias'>"
        
        # Genera los días del 1 al 31 para cada semana
        # range(1, 32) genera números del 1 al 31
        for dia in range(1, 32):
            cadena += f"{dia} "
            
            # Añado un separador visual (guion) si no es el último día
            if dia < 31:
                cadena += "- "
        
        cadena += "</td>"
        cadena += "</tr>"

    # Cierro las etiquetas HTML
    cadena += """
            </tbody>
        </table>
    </body>
    </html>
    """
    
    return cadena

if __name__ == "__main__":
    app.run(debug=True)