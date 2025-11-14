import json

ruta_blog = r"C:\Users\Usuario\Documents\DAM-2025\Ejercicios IA\PROGRAMACION\UD5-Lectura y escritura de información\002-Ficheros de datos. Registros\blog.json"

with open(ruta_blog, 'r', encoding='utf-8') as archivo:
    blog = json.load(archivo)

for articulo in blog:
    print("Título: " + articulo['titulo'])
    print("Fecha: " + articulo['fecha'])
    print("Autor: " + articulo['autor'])
    print("Contenido: " + articulo['contenido'])
    print("----------------------------------")