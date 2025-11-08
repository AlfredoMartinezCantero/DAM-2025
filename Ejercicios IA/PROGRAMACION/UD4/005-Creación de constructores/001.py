'''
Ejercicio 1: Repaso del constructor básico

Crea una clase Gato con un constructor básico.
El constructor debe asignar un valor inicial de 0 a la propiedad edad.
Agrega un método maulla que devuelva "El gato está maullando".
Crea un objeto gato1 y muestra su edad.

Ejercicio 2: Constructor con parámetros

Modifica la clase Gato para que acepte el parámetro edad en el constructor.
El valor de edad debe asignarse a la propiedad correspondiente.
Crea un objeto gato2 con una edad específica y muestra su edad.

Ejercicio 3: Cliente interactivo

Crea una clase Cliente que acepte cuatro parámetros: nombre, apellidos, email y direccion.
El constructor debe asignar estos valores a las propiedades correspondientes.
Pide al usuario que introduzca el nombre, apellidos, email y dirección del cliente.
Crea un objeto cliente1 con los datos proporcionados por el usuario.
'''

class Cliente():
    def __init__(self,nombre,apellidos,email,direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.direccion = direccion

nombre = input("Introduce el nombre del cliente: ")
print("")
apellidos = input("Introduce los apellidos del cliente: ")
print("")
email = input("Introduce el email del cliente: ")
print("")
direccion = input("Introduce la dirección del cliente: ")
print("")

cliente1 = Cliente(nombre,apellidos,email,direccion)
print("-----------------------------------------------------------------")
print("Nombre: ", cliente1.nombre)
print("")
print("Apellidos: ", cliente1.apellidos)
print("")
print("Email: ", cliente1.email)
print("")
print("Dirección: ", cliente1.direccion)
print("")