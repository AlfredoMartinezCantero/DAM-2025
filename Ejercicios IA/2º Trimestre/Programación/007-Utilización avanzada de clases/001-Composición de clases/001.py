class Cancion:
    #Se define el constructor
    def __init__(self, nombre, artista, duracion):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion

    #Devuelvo una cadena con los datos
    def dameDatos(self):
        return f"Canción: {self.nombre} / Artista: {self.artista} / Duración: {self.duracion} min"

class Extremoduro(Cancion):
    def __init__(self, nombre, artista, duracion):
        #Llamo al constructor del padre, en este caso vamos a nombrar Extremoduro "hijo" de la clase "Cancion"
        super().__init__(nombre, artista, duracion)
        self.genero = "Rock"

class Pop(Cancion):
    def __init__(self, nombre, artista, duracion):
        super().__init__(nombre, artista, duracion)
        self.ritmo = "Bailable"

#Creo una instancia de la clase Extremoduro
rock = Extremoduro("So Payaso", "Extremoduro", 4.5)

#Creo una instancia de la clase Pop
pop = Pop("Thriller", "Michael Jackson", 5.2)

#Imprimo la información usando el método heredado
print(rock.dameDatos())
print(pop.dameDatos())