class Matematicas():
    def __init__(self):
        self.PI = 3.14159265359
    
    def redondeo(self, numero):
        entero = int(numero)
        decimal = numero - entero
        if decimal < 0.5:
            redondeo = 0
        else:
            redondeo = 1
        return entero + redondeo

    def techo(self, numero):
        entero = int(numero)
        decimal = numero - entero
        if decimal > 0:
            techo = 1
        else:
            techo = 0
        return entero + techo

    def suelo(self, numero):
        entero = int(numero)
        return entero
    
Mate = Matematicas()
print("Redondeo de 4.7:", Mate.redondeo(4.7))
print("Redondeo de 4.2:", Mate.redondeo(4.2))
print("Valor al techo de 4.7:", Mate.techo(4.7))
print("Valor al suelo de 4.7:", Mate.suelo(4.7))