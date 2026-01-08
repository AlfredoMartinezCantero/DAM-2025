#Creamos diccionario principal que representa al músico
musico = {
    "nombre": "Roberto",
    "apellidos": "Iniesta",
    "discografia": [
        #Primer elemento de la lista
        {
            "nombre_album": "Rock Transgresivo",
            "año_lanzamiento": 1989
        },
        #Segundo elemento de la lista
        {
            "nombre_album": "Agila",
            "año_lanzamiento": 1996
        },
        #Tercer elemento de la lista
        {
            "nombre_album": "La Ley Innata",
            "año_lanzamiento": 2008
        }
    ]
}

#Imprimimos el diccionario completo para verificar la estructura
print(" ### Estructura Completa ### ")
print(musico)

#Accede e imprimir el nombre del primer álbum
nombre_primer_album = musico["discografia"][0]["nombre_album"]

print("\n### Consulta Específica ###")
print(f"El primer álbum de la lista es: {nombre_primer_album}")