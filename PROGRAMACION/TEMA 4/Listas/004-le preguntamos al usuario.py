# Declaramos una clase
class Cliente():
    def _init_(self):
        self.email = None # También se puede poner "" en vez de None
        self.nombre= None
        self.direccion = None

# Usamos la clase instanciando en un objeto
cliente1 = Cliente()
cliente1.email = input("Introduce el email del cliente: ")
cliente1.nombre = input("Introduce el nombre del cliente: ")
cliente1.direccion = input("Introduce la dirección del cliente: ")

print(cliente1)














