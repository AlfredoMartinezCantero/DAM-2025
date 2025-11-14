#En este ejercicio el uso de los `métodos estáticos` nos permite realizar operaciones no dependientes de una instancia concreta de la clase, sino del concepto de `TiendaMusica()`· Así pues el uso de un método estático facilita la reutilización del código, lo que hace que el programa sea más eficiente.
#Definimos la clase `TiendaMusica`, la cual contiene un método estático llamado `calcularCostoTotal`. Se toma como parámetro una lista de canciones y devuelve el coste total multiplicando la cantidad de canciones por un precio fijo por canción de 1.50€ cada una.

```
class TiendaMusica():
    PRECIO_POR_CANCION = 1.50

    @staticmethod
    def calcularCostoTotal(canciones):
        if canciones is None:
            return 0.0
        cantidad = len(canciones)
        total = round(cantidad * TiendaMusica.PRECIO_POR_CANCION, 2)
        return total

lista_canciones = ['Cancion A', 'Cancion B', 'Cancion C']
total = TiendaMusica.calcularCostoTotal(lista_canciones)
print("Cantidad canciones:", len(lista_canciones))
print("Precio unitario:", TiendaMusica.PRECIO_POR_CANCION, "€")
print("Coste total:", total, "€")
```

#En este ejercicio se relaciona directamente con los conceptos `clases y métodos estáticos` en programación orientada a objetos. Entendemos como un método estático puede representar una operación general de una clase sin depender de atributos específicos de cada objeto.
