# pip3 install pymysql
import pymysql

conn = pymysql.connect(
    host="127.0.0.1",        # Ahora funcionará tanto si pones esto...
    # host="localhost",      # ...como si pones esto.
    user="empresa2026",
    password="Empresa2026$", # ¡Ojo a la mayúscula y el $!
    database="empresa2026",
    charset="utf8mb4"
)

with conn.cursor() as cursor:
    cursor.execute("SELECT * FROM clientes")
    for row in cursor.fetchall():
        print(row)

conn.close()
