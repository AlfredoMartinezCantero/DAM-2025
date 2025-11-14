import zipfile
import os

#**1.- Crear un archivo con texto**
archivo = open("miarchivo.txt",'w')
archivo.write("Esto es un texto de prueba que estoy escribiendo")

archivo.close()

#**2.- Comprimir un archivo**
origen = 'crmca_crmcapitol (1).sql'
destino = 'basededatos.zip'

archivo = zipfile.ZipFile(destino, 'w')
archivo.write(origen)

archivo.close()

#**3.- Eliminar un archivo**
os.remove("miarchivo.txt")

#**4.- Crear una carpeta**
os.mkdir("micarpeta")

#**5.- Comprimir todos los archivos de una carpeta**
carpeta = 'archivos'
for directorio, subcarpetas, archivos in os.walk(carpeta):
    for nombre_archivo in archivos:
        origen = os.path.join(directorio, nombre_archivo)
        destino = os.path.join(directorio, nombre_archivo+ ".zip")
        archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
        archivo.write(origen, arcname=nombre_archivo)
        archivo.close()

#**6.- Comprimir una carpeta**
origen = 'archivos'
destino = 'archivos.zip'

archivozip = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
for directorio, carpetas, archivos in os.walk(origen):
    for archivo in archivos:
        rutaarchivo = os.path.join(directorio, archivo)
        rutarelativa = os.path.relpath(rutaarchivo, origen)
        archivozip.write(rutaarchivo, rutarelativa)
        archivozip.close()

