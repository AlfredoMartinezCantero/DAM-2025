import zipfile
import os

carpeta = "Prácticas-20251021T085100Z-1-001"

for directorio, subcarpetas, archivos in os.walk(carpeta):
    for nombre_archivo in archivos:
        origen = os.path.join(directorio, nombre_archivo)
        destino = os.path.join(directorio, nombre_archivo+ ".zip")
        archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
        archivo.write(origen, arcname=nombre_archivo)
