class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def dameDatos(self):
        #Añadimos un espacio para que no se junten ambos textos, sin esto se vería asi: Alfredo MartinezCantero
        return self.nombre + " " + self.apellidos

class Profesor(Persona):
    def __init__(self, nombre, apellidos):
        #Llamamos al constructor del padre para gestionar nombre y apellidos
        super().__init__(nombre, apellidos)

    def dameDatos(self):
        return "Profesor: " + self.nombre + " " + self.apellidos

class Alumno(Persona):
    def __init__(self, nombre, apellidos, email, direccion):
        #Inicializamos la parte común (Persona)
        super().__init__(nombre, apellidos)
        #Inicializamos la parte específica (Alumno)
        self.email = email
        self.direccion = direccion

    def dameDatos(self):
        return "Alumno: " + self.nombre + " " + self.apellidos + " | Email: " + self.email

#Instanciamos un Alumno pasando los 4 argumentos requeridos
alumno1 = Alumno("Alfredo", "Martínez Cantero", "alfredomartinezcantero@gmail.com", "La calle de Alfredo")
print(alumno1.dameDatos())

#Instanciamos un Profesor pasando los 2 argumentos requeridos
profesor1 = Profesor("Jose Vicente", "Carratalá")
print(profesor1.dameDatos())