import sqlite3

class BaseDeDatos:
    def __init__(self, nombre_servidor, base_de_datos, credenciales):
        self.nombre_servidor = nombre_servidor
        self.base_de_datos = base_de_datos
        self.credenciales = credenciales
        self.conexion = None

    def conectar(self):
        try:
            # Simulamos el uso de credenciales y servidor
            print(f"Intentando conectar a {self.base_de_datos} en {self.nombre_servidor}...")
            
            # Establecemos la conexión real
            self.conexion = sqlite3.connect(self.base_de_datos)
            
            print("Conexión establecida con éxito")
            
        except sqlite3.Error as error:
            # Capturamos cualquier error específico de la base de datos
            print(f"Error al conectar: {error}")

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada")
        else:
            print("No hay ninguna conexión abierta para cerrar.")

if __name__ == "__main__":
    # Definimos las credenciales
    usuario = "admin"
    password = "123" # No es real para SQLite
    
    # Instanciamos la clase
    mi_db = BaseDeDatos("localhost", "mi_base_prueba.db", (usuario, password))
    
    mi_db.conectar()
    mi_db.desconectar()