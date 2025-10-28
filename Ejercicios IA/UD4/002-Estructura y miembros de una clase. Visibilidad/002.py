#`class` sirve como plantilla para crear objetos, en este caso, creamos un Cliente con sus diferentes características(atributos) y comportamientos(métodos).
#`def __init__(self):` esto se llama **constructor** y es algo que Python ejecuta automáticamente cada vez que se crea un nuevo objeto de la clase, cumple la función de inicializar los atributos del objeto. Por otro lado, `self` es una referencia al propio objeto y sirve para marcar que X atributo pertenece al objeto en particular.
#`input` sirve para preguntar directamente al usuario un dato, por ejemplo: `input("Introduce tu email: ") esto hace que el usuario vea directamente en pantalla esta frase y le dice que introduzca su email para continuar al siguiente paso.
#Por último `print` que sirve para imprimir por pantalla lo que nosotros queramos de manera literal, de esta manera, si usamos print("Email:", cliente1.email) se mostrará por pantalla el email que la persona haya introducido.



class Cliente():
    def __init__(self):
        self.email = None
        self.nombre = None
        self.direccion = None

cliente1 = Cliente()
cliente1.email = input("Introduce tu email: ")
cliente1.nombre = input("Introduce tu nombre: ")
cliente1.direccion = input("Introduce tu dirección: ")
print("---------------------------------------------")
print("Email:", cliente1.email)
print("Nombre:", cliente1.nombre)
print("Dirección:", cliente1.direccion)



#Este ejercicio nos enseña a crear una clase, definir atributos, instanciar un objeto y asignar valores mediante la entrada del usuario. Estos conceptos se relacionan directamente con la programación orientada a objetos.
