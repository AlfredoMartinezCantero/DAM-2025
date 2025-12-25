import random
import json
from flask import Flask, render_template
import math  # Para poder hacer trigonometría

class Npc():
    def __init__(self, x, y, radio, direccion, velocidad):
        self.posx = x
        self.posy = y
        self.radio = radio
        self.direccion = direccion   # Dirección = ángulo en radianes
        self.velocidad = velocidad

    # Método para convertir el objeto en diccionario
    def to_dict(self):
        return {
            "posx": self.posx,
            "posy": self.posy,
            "radio": self.radio,
            "direccion": self.direccion
        }

    def mover(self):
        # Variar un poco la dirección cada frame
        self.direccion += (random.random() - 0.5) * 0.2

        # Actualizar posición con trigonometría
        self.posx += math.cos(self.direccion) * self.velocidad
        self.posy += math.sin(self.direccion) * self.velocidad


# Preparo los personajes
personajes = []
numero_personajes = 500

for i in range(numero_personajes):
    xaleatoria = random.randint(0, 500)
    yaleatoria = random.randint(0, 500)
    radioaleatorio = random.randint(10, 30)
    direccionaleatoria = random.random() * math.pi * 2
    velocidadaleatoria = random.random() * 5

    personajes.append(Npc(
        xaleatoria,
        yaleatoria,
        radioaleatorio,
        direccionaleatoria,
        velocidadaleatoria
    ))

# Lanzo una web
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("juego.html")

@app.route("/api")
def api():
    # Primero muevo todos los personajes
    for personaje in personajes:
        personaje.mover()

    personajes_json = [p.to_dict() for p in personajes]
    return json.dumps(personajes_json, indent=2)

if __name__ == "__main__":
    app.run(debug=True)

