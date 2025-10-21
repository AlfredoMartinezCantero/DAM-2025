'''
Quiero:
1.-Pedir al usuario una ruta de una carpeta con input
2.-Repasar todas las subcarpetas y archivos dentro de esa carpeta
3.-Para cada archivo o carpeta, quiero comprimirla en un ZIP
4.-Una vez comprimido ese zip, quiero eliminar los contenidos originales
'''

import os
import zipfile

# 1.-Pedir al usuario una ruta de una carpeta con input
ruta_carpeta = input("Introduce la ruta de la carpeta a procesar: ")

# Asegurarse de que la ruta existe antes de continuar
if not os.path.isdir(ruta_carpeta):
    print(f"Error: La ruta '{ruta_carpeta}' no es una carpeta válida o no existe.")
else:
    # 2.-Repasar todas las subcarpetas y archivos dentro de esa carpeta
    # Recorre el directorio sin entrar en subdirectorios de subdirectorios (solo el nivel inmediatamente inferior)
    for nombre_item in os.listdir(ruta_carpeta):
        ruta_completa_item = os.path.join(ruta_carpeta, nombre_item)
        
        # 3.-Para cada archivo o carpeta, quiero comprimirla en un ZIP
        # Define el nombre del archivo ZIP
        nombre_zip = ruta_completa_item + ".zip"
        
        try:
            # Crea el archivo ZIP
            print(f"Comprimiendo '{nombre_item}' en '{nombre_zip}'...")
            archivo_zip = zipfile.ZipFile(nombre_zip, 'w', compression=zipfile.ZIP_DEFLATED)
            
            # Comprime el archivo o carpeta
            if os.path.isfile(ruta_completa_item):
                # Es un archivo
                archivo_zip.write(ruta_completa_item, arcname=nombre_item)
            elif os.path.isdir(ruta_completa_item):
                # Es una carpeta. Recorre el contenido para comprimirlo
                for root, dirs, files in os.walk(ruta_completa_item):
                    for file in files:
                        ruta_archivo = os.path.join(root, file)
                        # Calcula la ruta relativa dentro del ZIP (nombre de la carpeta/archivos...)
                        ruta_relativa = os.path.relpath(ruta_archivo, os.path.dirname(ruta_completa_item))
                        archivo_zip.write(ruta_archivo, arcname=ruta_relativa)
            
            # Cierra el archivo ZIP
            archivo_zip.close()
            print("Compresión completada.")
            
            # 4.-Una vez comprimido ese zip, quiero eliminar los contenidos originales
            if os.path.isfile(ruta_completa_item):
                # Elimina el archivo
                os.remove(ruta_completa_item)
                print(f"Archivo original '{nombre_item}' eliminado.")
            elif os.path.isdir(ruta_completa_item):
                # Elimina la carpeta y todo su contenido
                import shutil
                shutil.rmtree(ruta_completa_item)
                print(f"Carpeta original '{nombre_item}' y su contenido eliminados.")
            
        except Exception as e:
            print(f"Ocurrió un error al procesar '{nombre_item}': {e}")
