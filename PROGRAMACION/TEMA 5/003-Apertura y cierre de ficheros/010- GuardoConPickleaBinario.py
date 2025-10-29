import pickle

class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail

clientes = []

clientes.append(Cliente("Alfredo Martinez","alfredomartinezcantero@gmail.com"))
clientes.append(Cliente("Paco","paco@gmail.com"))

archivo = open("clientes.bin","wb")
pickle.dump(clientes,archivo)
archivo.close()

