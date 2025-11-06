def conectar_base_de_datos():
    print("")
    print("Intentando conectar a la base de datos...")
    print("")
    try:
        resultado = 10 / 0
        print("Hemos conectado con la base de datos!")
    except:
        print("Ooops... Ha ocurrido un error al conectarse a la base de datos.")
        print("")
        print("Por favor, verifica tu conexión a internet y vuelve a intentarlo.")

conectar_base_de_datos()
print("")
print("El programa sigue ejecutándose...")
print("")