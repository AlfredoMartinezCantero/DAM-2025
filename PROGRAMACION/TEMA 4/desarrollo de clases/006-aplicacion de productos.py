# Las propiedades son como las variables PERO dentro de una clase

class Cliente():
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.telefonos = []

# Ahora instancio un nuevo objeto
cliente1 = Cliente()

# Ahora le escribo una propiedad

cliente1.nombre = "Alfredo"

print("El nombre del cliente es: ", cliente1.nombre)

cliente1.telefonos.append("123456")
cliente1.telefonos.append("654321")

print(cliente1.telefonos)









