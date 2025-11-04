class Cliente():
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def setEmail(self, nuevoemail):
        self.email = nuevoemail
    
    def getEmail(self):
        return self.email
   
cliente1 = Cliente("Álvaro", "Martínez", "alvaromartinez@gmail.com")
cliente2 = Cliente("Mónica", "Sanchez", "monicasanchez@gmail.com")
cliente3 = Cliente("Rafa", "Trullenque", "rafatrullenque@gmail.com")    

print("")
print("Email original del Cliente 1:", cliente1.getEmail())
cliente1.setEmail("alvaro2000@gmail.com")   
print("Nuevo email del cliente 1:", cliente1.getEmail())
print("")
print("")
print("Email original del Cliente 2:", cliente2.getEmail())
cliente2.setEmail("monicaprogramadora@gmail.com")
print("Nuevo email del cliente 2:", cliente2.getEmail())
print("")
print("")
print("Email original del Cliente 3:", cliente3.getEmail())
cliente3.setEmail("racantru@gmail.com")
print("Nuevo email del cliente 3:", cliente3.getEmail())
