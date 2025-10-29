class Gato:
    def __init__(self): ""   # Esto es una propiedad
    
    def maulla(self):        # Esto es un método (una acción)
        return "miau"


    def setColor(self,nuevocolor):  # Defino un setter - el método es el responsable de cambiar la propiedad
        
        # Por ejemplo aquí podría validar si el color es un color válido para un gato
        
        self.color = nuevocolor     # Y cambio la propiedad


gato1 = Gato()
gato1.color = "naranja"     # Aquí seteamos una propiedad directamente (no es buena práctica)

gato1.setColor("naranja")    # Esto es una práctica mucho mejor

print(gato1.maulla())       # Aquí llamamos un método









