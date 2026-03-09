import sqlite3

def main():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                telefono TEXT
            )
        ''')
        
        while True:
            print("\n1. Crear cliente")
            print("2. Listar clientes")
            print("3. Actualizar cliente")
            print("4. Borrar cliente")
            print("5. Salir")
            
            try:
                opcion = int(input("Selecciona una opción: "))
                
                if opcion == 1:
                    nombre = input("Nombre: ")
                    email = input("Email: ")
                    telefono = input("Teléfono (opcional): ")
                    cursor.execute('INSERT INTO clientes (nombre, email, telefono) VALUES (?, ?, ?)', (nombre, email, telefono))
                    conn.commit()
                    
                elif opcion == 2:
                    cursor.execute('SELECT * FROM clientes')
                    clientes = cursor.fetchall()
                    for cliente in clientes:
                        print(cliente)
                        
                elif opcion == 3:
                    id_cliente = int(input("ID del cliente a actualizar: "))
                    nombre = input("Nuevo nombre: ")
                    email = input("Nuevo email: ")
                    telefono = input("Nuevo teléfono (opcional): ")
                    cursor.execute('UPDATE clientes SET nombre=?, email=?, telefono=? WHERE id=?', (nombre, email, telefono, id_cliente))
                    conn.commit()
                    
                elif opcion == 4:
                    id_cliente = int(input("ID del cliente a borrar: "))
                    cursor.execute('DELETE FROM clientes WHERE id=?', (id_cliente,))
                    conn.commit()
                    
                elif opcion == 5:
                    break
                
                else:
                    print("Opción no válida")
                    
            except EOFError:
                break
    
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        conn.close()

if __name__ == "__main__":
    main()