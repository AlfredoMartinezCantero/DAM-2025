import mysql.connector
import matplotlib.pyplot as pt

conexion = mysql.connector.connect(
    host="172.27.59.229",
    user="clientes",  
    password="Clientes123$",
    database="clientes"
)

cursor = conexion.cursor()            
cursor.execute('''
    SELECT 
    COUNT(stock) AS numero,
    stock
    FROM productos
    GROUP BY color
    ORDER BY numero DESC;    
''')         # Ordenamos por numero

filas = cursor.fetchall()   
cantidades = []
etiquetas = []
for fila in filas:
    cantidades.append(fila[0])
    etiquetas.append(fila[1])
print(cantidades)
print(etiquetas)
pt.pie(cantidades,labels=etiquetas)
pt.show()