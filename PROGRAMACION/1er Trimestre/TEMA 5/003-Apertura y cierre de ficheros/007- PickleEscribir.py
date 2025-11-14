import pickle
# pip3 install pickle (linux)
# pip install pickle (windows)

archivo = open("datos.bin","wb") # WB = write binarie
cadena = "Alfredo Martinez"

pickle.dump(cadena,archivo)
archivo.close()








