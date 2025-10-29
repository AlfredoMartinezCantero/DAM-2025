class CLiente():
    def __init__(self,nombre,apellidos,email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        
print("###### Gestión de clientes v0.1 ######")
print("#### Alfredo Martínez Cantero ####")

clientes = []

while True:
    print("Escoge una opción:")
    print("1.-Insertar un cliente")
    print("2.-Listar un cliente")
    print("3.-Actualizar un cliente")
    print("4.-Eliminar un cliente")
    opcion = int(input("Escoge una opción: "))
    
    
