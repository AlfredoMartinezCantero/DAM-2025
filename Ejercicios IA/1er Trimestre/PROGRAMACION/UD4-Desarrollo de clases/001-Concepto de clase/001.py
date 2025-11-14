#`class` sirve como plantilla para crear objetos, en este caso, creamos Gatos con sus diferentes características(atributos) y comportamientos(métodos).
#`def __init__(self):` esto se llama ***constructor*** y es algo que Python ejecuta automáticamente cada vez que se crea un nuevo objeto de la clase, cumple la función de inicializar los atributos del objeto. Por otro lado, `self` es una referencia al propio objeto y sirve para marcar que X atributo pertenece al objeto en particular.
#`def maulla(self):` Igual que en el anterior `def`este sigue siendo un método, es decir, una acción o comportamiento del objeto, en este caso simplemente imprime un mensaje cuando se llama al objeto con `print("El gatito está maullando")`



class Gato():
    def __init__(self):
        self.color = ""
        self.edad = 0
    def maulla(self):
        print("El gatito está maullando")
        
Misifu = Gato()
Misifu.color = "crema"
Misifu.edad = 9
Misifu.maulla()

Pascal = Gato()
Pascal.color = "gris"
Pascal.edad = 11
Pascal.maulla()

#Las clases son fundamentales en la programación orientada a objetos pues nos permiten organizar el código de manera clara, en lugar de repetir el mismo código para cada "gato", definimos una sola vez la estructura y comportamiento de la clase para a continuación crear todos los "gatos" que necesitemos con sus características.
