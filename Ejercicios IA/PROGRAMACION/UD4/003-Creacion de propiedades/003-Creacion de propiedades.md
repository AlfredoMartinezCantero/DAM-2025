# Introducción:
---
En este ejercicio aprenderemos a crear una clases, definir sus atributos principales, instanciar un objeto de esa clase y mostrar información al usuario. 

`class` sirve como plantilla para crear objetos. En este caso, creamos un **Producto** con sus diferentes características (atributos) y comportamientos (métodos).

`def __init__(self, nombre, precio):` es el **constructor** de la clase y se ejecuta automáticamente al crear un nuevo objeto. Su función es inicializar los atributos del objeto con los valores que le pasamos como parámetros.

`self` hace referencia al propio objeto, y permite acceder o modificar sus atributos.

`print` sirve para mostrar información por pantalla, mientras que `for` se usa para recorrer una lista y mostrar cada elemento.

---
```
class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

producto1 = Producto("Ordenador portátil", 1200€)
print("Nombre del producto:", producto1.nombre)

productos = ["Ordenador portátil", "Teléfono móvil", "Tablet", "Monitor"]
print("Productos disponibles:")
for producto in productos:
    print("-", producto)
```
---
# Conclusión
Este ejercicio nos enseña cómo crear clases, definir y leer atributos, instanciar objetos y trabajar con listas.

Algunos errores comunes al hacer este ejercicio pudiera ser el olvidar usar el `self` o en la lista global usar `()`en vez de `[]`.