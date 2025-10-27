import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import mysql.connector
from tkinter import messagebox

# --- Conexión a la base de datos ---
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()

# --- Ventana principal ---
ventana = ttk.Window(themename="superhero")  # puedes probar otros temas: "flatly", "darkly", "cyborg", etc.
ventana.title("Gestión de Clientes - Empresadam")
ventana.geometry("800x600")

# --- Función para insertar clientes ---
def insertar():
    dni = DNINIE.get()
    nom = nombre.get()
    ape = apellidos.get()
    mail = email.get()

    if not (dni and nom and ape and mail):
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
        return

    try:
        cursor.execute(
            "INSERT INTO clientes (DNINIE, nombre, apellidos, email) VALUES (%s, %s, %s, %s)",
            (dni, nom, ape, mail)
        )
        conexion.commit()
        messagebox.showinfo("Éxito", "Cliente insertado correctamente.")
        actualizar_tabla()
        DNINIE.delete(0, "end")
        nombre.delete(0, "end")
        apellidos.delete(0, "end")
        email.delete(0, "end")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo insertar el cliente:\n{err}")

# --- Función para actualizar el Treeview ---
def actualizar_tabla():
    for fila in arbol.get_children():
        arbol.delete(fila)
    cursor.execute("SELECT * FROM clientes;")
    filas = cursor.fetchall()
    for fila in filas:
        arbol.insert("", "end", values=fila)

# --- Frame del formulario ---
frame_form = ttk.Labelframe(ventana, text="Agregar nuevo cliente", padding=20)
frame_form.pack(fill=X, padx=20, pady=20)

# Campos del formulario
ttk.Label(frame_form, text="DNI/NIE del cliente:").pack(anchor=W)
DNINIE = ttk.Entry(frame_form, width=40)
DNINIE.pack(pady=5)

ttk.Label(frame_form, text="Nombre del cliente:").pack(anchor=W)
nombre = ttk.Entry(frame_form, width=40)
nombre.pack(pady=5)

ttk.Label(frame_form, text="Apellidos del cliente:").pack(anchor=W)
apellidos = ttk.Entry(frame_form, width=40)
apellidos.pack(pady=5)

ttk.Label(frame_form, text="Email del cliente:").pack(anchor=W)
email = ttk.Entry(frame_form, width=40)
email.pack(pady=5)

ttk.Button(frame_form, text="Insertar cliente", command=insertar, bootstyle=SUCCESS).pack(pady=10)

# --- Tabla (Treeview) ---
frame_tabla = ttk.Labelframe(ventana, text="Lista de clientes", padding=10)
frame_tabla.pack(fill=BOTH, expand=True, padx=20, pady=10)

arbol = ttk.Treeview(frame_tabla, columns=("DNINIE", "nombre", "apellidos", "email"), show="headings", height=10)
arbol.heading("DNINIE", text="DNI/NIE")
arbol.heading("nombre", text="Nombre")
arbol.heading("apellidos", text="Apellidos")
arbol.heading("email", text="Email")

# Ajustar tamaño de columnas
arbol.column("DNINIE", width=100)
arbol.column("nombre", width=150)
arbol.column("apellidos", width=200)
arbol.column("email", width=200)

# Scrollbar vertical
scroll = ttk.Scrollbar(frame_tabla, orient="vertical", command=arbol.yview)
arbol.configure(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
arbol.pack(fill=BOTH, expand=True)

# --- Cargar datos iniciales ---
actualizar_tabla()

ventana.mainloop()

