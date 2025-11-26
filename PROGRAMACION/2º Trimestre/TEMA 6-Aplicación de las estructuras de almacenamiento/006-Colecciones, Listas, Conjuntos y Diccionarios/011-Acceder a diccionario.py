persona = {
    "nombre":"Alfredo",
    "apellidos":"Martínez Cantero",
    "correo":"alfredo@gmail.com",
    "edad":24,
    "telefonos":[
        {
            "tipo":"fijo",
            "número":96345678
        },
        {
            "tipo":"movil",
            "número":12345678
        }
    ]
}

print(persona)
print(persona["telefonos"][0]["número"])