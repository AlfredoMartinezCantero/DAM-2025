class Animal():
    def __init__(self,edad,nombre,raza):
        self.edad = edad
        self.nombre = nombre
        self.raza = raza

class Gato(Animal):
    def __init__(self,edad,nombre,raza):
        super().__init__(edad,nombre,raza)

class Perro(Animal):
    def __init__(self,edad,nombre,raza):
        super().__init__(edad,nombre,raza)

gato1 = Gato(2, "Pascal", "Siames")
print("El gato se llama", gato1.nombre, "y tiene", gato1.edad, "años")

perro1 = Perro(4, "Madacascar", "Golden retriever")
print("El perro se llama", perro1.nombre, "y tiene", perro1.edad, "años")