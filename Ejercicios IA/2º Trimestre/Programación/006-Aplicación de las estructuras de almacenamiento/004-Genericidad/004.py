#Definimos una lista
numeros = [1, 2, 3, 4, "hola", "5", "mundo"]

#Creamos una función para calcular el doble
def calculaDoble(lista):

    #Recorremos cada elemento de la lista
    for elemento in lista:
        try:
            #Intentamos pasar el númer a entero y multiplicarlo por 2
            #Si el elemento no es un número
            resultado = int(elemento)* 2
            print(resultado)
        except:
            #Si falla la conversión el programa mostrará por pantalla "un error"    
            print("El resultado no és válido")
#Por último llamamos a la función
calculaDoble(numeros)