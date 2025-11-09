#-- Crear la Tabla.
#CREATE TABLE clientes (
 #   Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
  #  nombre TEXT NOT NULL,
   # apellidos TEXT NOT NULL,
    #email TEXT NOT NULL UNIQUE
#);

# Script Python para gestionar clientes en SQLite
import sqlite3
from sqlite3 import Error

DB_NAME = 'empresa.db'
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
def create_table(conn):
    try:
        sql_create_clients_table = """ CREATE TABLE IF NOT EXISTS clientes (
                                        Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nombre TEXT NOT NULL,
                                        apellidos TEXT NOT NULL,
                                        email TEXT NOT NULL UNIQUE
                                    ); """
        c = conn.cursor()
        c.execute(sql_create_clients_table)
    except Error as e:
        print(e)
def create_client(conn, client):
    sql = ''' INSERT INTO clientes(nombre,apellidos,email)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, client)
    conn.commit()
    return cur.lastrowid
def list_clients(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes")
    rows = cur.fetchall()
    for row in rows:
        print(row)
def update_client(conn, client):
    sql = ''' UPDATE clientes
              SET nombre = ? ,
                  apellidos = ? ,
                  email = ?
              WHERE Identificador = ?'''
    cur = conn.cursor()
    cur.execute(sql, client)
    conn.commit()
def delete_client(conn, id):
    sql = 'DELETE FROM clientes WHERE Identificador=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
def main():
    database = DB_NAME
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        while True:
            print("Gestión de Clientes")
            print("1. Crear Cliente")
            print("2. Listar Clientes")
            print("3. Actualizar Cliente")
            print("4. Eliminar Cliente")
            print("5. Salir")
            choice = input("Selecciona una opción: ")
            if choice == '1':
                nombre = input("Nombre: ")
                apellidos = input("Apellidos: ")
                email = input("Email: ")
                client = (nombre, apellidos, email)
                create_client(conn, client)
                print("Cliente creado.")
            elif choice == '2':
                list_clients(conn)
            elif choice == '3':
                id = int(input("ID del cliente a actualizar: "))
                nombre = input("Nuevo Nombre: ")
                apellidos = input("Nuevos Apellidos: ")
                email = input("Nuevo Email: ")
                client = (nombre, apellidos, email, id)
                update_client(conn, client)
                print("Cliente actualizado.")
            elif choice == '4':
                id = int(input("ID del cliente a eliminar: "))
                delete_client(conn, id)
                print("Cliente eliminado.")
            elif choice == '5':
                break
            else:
                print("Opción no válida.")