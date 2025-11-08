import pickle

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

clientes = [
    Cliente("Alfredo Martínez", "alfredo@gmail.com"),
    Cliente("Rafa Cantero", "rafa@gmail.com")
]

with open("clientes.bin", "wb") as archivo:
    pickle.dump(clientes, archivo)

print("Lista de clientes guardada en 'clientes.bin'")