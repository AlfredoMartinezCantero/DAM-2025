'''
Aplicación de gestión de productos
(c) 2025 Alfredo Martínez Cantero
Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0

# Creamos las variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v0.1, Alfredo Martínez Cantero")
# Le mostramos al usuario las opciones que tiene
print("Selecciona una opción:")
print("1.-Crear un nuevo producto")
print("2.-Listar productos")
print("3.-Actualizar productos")
print("4.- Eliminar productos")
opcion = int(input("Escoge tu opción: "))
# En función de la opción que coja el usuario
if opcion == 1:
    # O bien creamos un nuevo producto
    # O bien listamos los productos
    # O bien actualizamos los productos
    # O bien eliminamos los productos
# Y volvemos a repetir






