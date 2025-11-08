class Cliente:
    def __init__(self, nombrecompleto, email):
        self.__nombrecompleto = nombrecompleto
        self.__email = email

    def setNombreCompleto(self, nuevonombre):
        self.__nombrecompleto = nuevonombre
    def setEmail(self,nuevoemail):
        self.__email = nuevoemail
    
    def getNombreCompleto(self):
        return self.__nombrecompleto
    def getEmail(self):
        return self.__email

cliente1 = Cliente("Alfredo Martínez Cantero", "alfredomartinezcantero@gmail.com")
cliente1.setNombreCompleto("Alfredo Martínez Cantero")
cliente1.setEmail("alfredomartinezcantero@gmail.com")

print(cliente1.getNombreCompleto())
print(cliente1.getEmail())
