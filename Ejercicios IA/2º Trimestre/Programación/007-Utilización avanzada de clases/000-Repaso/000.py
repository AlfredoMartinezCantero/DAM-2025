import math
import random
import json
import pygame
from flask import Flask, render_template

pygame.init()
try:
    pass 
except:
    print("Advertencia: No se encontró el archivo de audio o dispositivo.")

class Npc:
    def __init__(self):
        self.posx = random.randint(0, 800)
        self.posy = random.randint(0, 600)
        self.radio = random.randint(10, 30)
        self.direccion = random.random() * math.pi * 2
        self.velocidad = random.uniform(1, 3)

    def mover(self):
        self.direccion += (random.random() - 0.5) * 0.2
        
        self.posx += math.cos(self.direccion) * self.velocidad
        self.posy += math.sin(self.direccion) * self.velocidad

        if self.posx < 0 or self.posx > 800:
            self.direccion = math.pi - self.direccion
        if self.posy < 0 or self.posy > 600:
            self.direccion = -self.direccion

    def to_dict(self):
        return {
            "x": round(self.posx, 2),
            "y": round(self.posy, 2),
            "radio": self.radio
        }

# Generación de la lista de 50 personajes
personajes = []
for i in range(50):
    personajes.append(Npc())

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("juego.html")

@app.route("/api")
def api():
    lista_json = []
    for p in personajes:
        p.mover()
        lista_json.append(p.to_dict())
    
    return json.dumps(lista_json)

if __name__ == "__main__":
    app.run(debug=True)