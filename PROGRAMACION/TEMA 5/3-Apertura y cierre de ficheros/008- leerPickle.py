import pickle
# pip3 install pickle (linux)
# pip install pickle (windows)

archivo = open("datos.bin","rb") # RB = read binarie

cadena = pickle.load(archivo)
print(cadena)

archivo.close()








