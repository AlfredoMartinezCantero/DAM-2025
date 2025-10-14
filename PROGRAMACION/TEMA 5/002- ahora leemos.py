archivo = open("clientes.txt",'r')  # r = read

contenido = archivo.readline()
# También existe archivo.readlines()

print(contenido)

archivo.close
