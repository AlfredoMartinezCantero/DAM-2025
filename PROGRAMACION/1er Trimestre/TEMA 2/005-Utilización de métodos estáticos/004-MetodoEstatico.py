class Matematicas():
    def __init__(self): # No es necesario al tener el staticmethod
        self.numero = 0 # No es necesario al tener el staticmethod
    @statichmethod
    def suma(a,b):
        return a+b
        
print(Matematicas.suma(6,7))
