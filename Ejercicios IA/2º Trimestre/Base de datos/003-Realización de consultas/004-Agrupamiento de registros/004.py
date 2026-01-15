import mysql.connector
import matplotlib.pyplot as plt

config = {
    'host': 'localhost',
    'user': 'admin_bara',      
    'password': 'BarBara_2025$',
    'database': 'Bar_Bara'     
}

def obtener_datos_agrupados(criterio_agrupacion):
    """
    Conecta a la BD y devuelve etiquetas y valores según el criterio.
    Criterio puede ser 'categoria' o 'color' (si existiera esa columna).
    """
    etiquetas = []
    valores = []
    
    try:
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()
        
        sql = f"SELECT {criterio_agrupacion}, COUNT(*) as total FROM producto GROUP BY {criterio_agrupacion}"
        
        cursor.execute(sql)
        resultados = cursor.fetchall()
        
        # Separamos en dos listas (ejes X e Y)
        for fila in resultados:
            etiquetas.append(fila[0]) # Ej: 'Cervezas', 'Vinos'
            valores.append(fila[1])   # Ej: 10, 5
            
        cursor.close()
        conexion.close()
        
        return etiquetas, valores

    except mysql.connector.Error as err:
        print(f"Error de conexión o consulta SQL: {err}")
        return [], []

def generar_grafico_barras(etiquetas, valores):
    print("Generando gráfico de barras por Categoría...")
    
    # Creo el gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(etiquetas, valores, color='skyblue')
    
    # Personalización
    plt.xlabel('Categorías')
    plt.ylabel('Número de Productos')
    plt.title('Stock de Productos por Categoría')
    
    # Muestro el gráfico
    plt.show()

def generar_grafico_circular(etiquetas, valores):
    print("Generando gráfico circular...")
    
    plt.figure(figsize=(8, 8))
    # muestra el porcentaje automáticamente
    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=140)
    
    plt.title('Distribución del Inventario')
    plt.show()

if __name__ == "__main__":
    
    # Agrupamiento por categoría
    print("--- CONSULTA 1: Agrupando por Categoría ---")
    cats, cantidades = obtener_datos_agrupados('categoria')
    
    if cats:
        generar_grafico_barras(cats, cantidades)
    else:
        print("No se encontraron datos para categorías.")

    # Agrupamiento por color 
    print("\n--- CONSULTA 2: Visualización Circular ---")
    
    if cats: 
        generar_grafico_circular(cats, cantidades)