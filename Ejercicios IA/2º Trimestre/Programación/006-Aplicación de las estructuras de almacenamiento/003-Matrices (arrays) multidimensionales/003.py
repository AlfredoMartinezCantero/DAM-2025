import pickle

# Creamos una lista de discos
discografia = [
    ["Robe", "Mayéutica", "Interludio"],
    ["AC/DC", "The Razors Edge", "Thunderstruck"]
]

# Recorremos la lista de discos
for disco in discografia:
    print(f"Artista: {disco[0]}, Álbum: {disco[1]}, Canción Favorita: {disco[2]}")

# Almacenamos la lista en un archivo binario
with open("discografia.bin", "wb") as archivo:
    pickle.dump(discografia, archivo)

# Recuperamos la lista desde el archivo binario
with open("discografia.bin", "rb") as archivo:
    discografia_recuperada = pickle.load(archivo)

for disco in discografia_recuperada:
    print(f"Artista: {disco[0]}, Álbum: {disco[1]}, Canción Favorita: {disco[2]}")