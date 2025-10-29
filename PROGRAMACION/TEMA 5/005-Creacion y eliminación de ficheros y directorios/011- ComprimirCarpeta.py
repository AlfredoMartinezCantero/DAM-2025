import zipfile
import os

origen = "Prácticas-20251021T085100Z-1-001" # Esto es el nombre de la carpeta que queremos comprimir
destino = "archivos.zip"

archivozip = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
for directorio, carpetas, archivos in os.walk(origen):
    for archivo in archivos:
        rutaarchivo = os.path.join(directorio, archivo)
        rutarelativa = os.path.relpath(rutaarchivo, origen)
        archivozip.write(rutaarchivo, rutarelativa)

archivozip.close()
