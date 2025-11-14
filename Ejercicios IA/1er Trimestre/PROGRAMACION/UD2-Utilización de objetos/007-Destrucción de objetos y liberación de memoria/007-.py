#Definimos una clase llamada Tarea. Esta clase tiene un atributo que guarda el nombre y un método que muestra un mensaje indicando que se está realizando esa tarea.
#Luego se crean dos objetos de la clase Tarea, escuchar música y jugar videojuegos.
#Este ejercicio nos hace comprender cómo las clases y objetos en Python permiten modelar diferentes actividades.
#El método __init__ sirve como constructor de una clase.

```
class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre

    def realizar(self):
        print("Estoy", self.nombre)
```

tarea1 = Tarea("escuchando música")
tarea2 = Tarea("jugando videojuegos")

tarea1.realizar()
tarea2.realizar()

#Un error común sería no usar el `self` tras poner el constructor `__init__` o no sangrar correctamente las líneas de código.
