class Cliente():
    def __init__(self,nuevonombre,nuevoemail):
        self.nombre = nuevonombre
        self.email = nuevoemail

clientes = []

clientes.append(Cliente("Alfredo Martinez","alfredomartinezcantero@gmail.com"))
clientes.append(Cliente("Paco","paco@gmail.com"))

print(clientes)


