import sqlite3
import os
import time
import sys

# === COLORES ANSI ===
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDER = "\033[4m"
DIM = "\033[2m"

# Paleta personalizada
CYAN = "\033[38;5;81m"
BLUE = "\033[38;5;39m"
GREEN = "\033[38;5;82m"
YELLOW = "\033[38;5;226m"
RED = "\033[38;5;203m"
MAGENTA = "\033[38;5;213m"
WHITE = "\033[97m"
GRAY = "\033[90m"

# === FUNCIONES DE INTERFAZ ===
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def escribir_lento(texto, velocidad=0.02):
    """Simula escritura progresiva."""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()

def banner():
    limpiar()
    gradient = [MAGENTA, BLUE, CYAN]
    texto = "★ AGENDA PROFESIONAL SQLITE ★"
    print()
    for i, c in enumerate(texto):
        color = gradient[i % len(gradient)]
        sys.stdout.write(f"{color}{BOLD}{c}{RESET}")
        sys.stdout.flush()
        time.sleep(0.01)
    print(f"\n{DIM}by Alfredo Martínez Cantero{RESET}")
    print(f"{CYAN}{'═'*70}{RESET}\n")

def linea(color=CYAN):
    print(f"{color}{'─'*70}{RESET}")

def tabla_clientes():
    cursor.execute("SELECT * FROM clientes ORDER BY Identificador ASC")
    filas = cursor.fetchall()
    if not filas:
        print(f"{YELLOW}⚠️  No hay clientes registrados aún.{RESET}\n")
        return

    ancho_id, ancho_nombre, ancho_apellidos, ancho_email = 4, 16, 22, 28
    print(f"{CYAN}╭{'─'*68}╮{RESET}")
    print(f"{CYAN}│{RESET} {BOLD}{'ID':<{ancho_id}}{' '*2}{'NOMBRE':<{ancho_nombre}}{' '*2}{'APELLIDOS':<{ancho_apellidos}}{' '*2}{'EMAIL':<{ancho_email}} {CYAN}│{RESET}")
    print(f"{CYAN}├{'─'*68}┤{RESET}")

    for fila in filas:
        print(f"{CYAN}│{RESET} {fila[0]:<{ancho_id}}  {fila[1]:<{ancho_nombre}}  {fila[2]:<{ancho_apellidos}}  {fila[3]:<{ancho_email}} {CYAN}│{RESET}")
    print(f"{CYAN}╰{'─'*68}╯{RESET}\n")

def animacion_salida():
    limpiar()
    escribir_lento(f"{MAGENTA}{BOLD}👋 Cerrando sesión...{RESET}", 0.04)
    time.sleep(0.4)
    for i in range(3):
        sys.stdout.write(f"{'.'*(i+1)} ")
        sys.stdout.flush()
        time.sleep(0.4)
    limpiar()
    print(f"{MAGENTA}{BOLD}✨ Adieu mon ami! Hasta la próxima.{RESET}\n")

# === CONFIGURACIÓN BASE DE DATOS ===
conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    email TEXT NOT NULL
);
""")
conexion.commit()

def reenumerar_ids():
    cursor.execute("SELECT nombre, apellidos, email FROM clientes ORDER BY Identificador ASC")
    clientes = cursor.fetchall()
    cursor.execute("DROP TABLE IF EXISTS clientes_temp")
    cursor.execute("""
        CREATE TABLE clientes_temp (
            Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            email TEXT NOT NULL
        );
    """)
    cursor.executemany("INSERT INTO clientes_temp (nombre, apellidos, email) VALUES (?, ?, ?)", clientes)
    cursor.execute("DROP TABLE clientes")
    cursor.execute("ALTER TABLE clientes_temp RENAME TO clientes")
    conexion.commit()

# === PROGRAMA PRINCIPAL ===
while True:
    banner()
    print(f"{BOLD}Menú Principal{RESET}")
    print(f"{BLUE}1.{RESET} ➕ Crear cliente")
    print(f"{BLUE}2.{RESET} 📋 Listar clientes")
    print(f"{BLUE}3.{RESET} ✏️  Actualizar cliente")
    print(f"{BLUE}4.{RESET} ❌ Eliminar cliente")
    print(f"{BLUE}5.{RESET} 🚪 Salir\n")
    linea()

    try:
        opcion = int(input(f"{BOLD}Selecciona una opción → {RESET}"))
    except ValueError:
        print(f"{RED}❌ Introduce un número del 1 al 5.{RESET}")
        time.sleep(1.2)
        continue

    # === CREAR CLIENTE ===
    if opcion == 1:
        limpiar()
        banner()
        print(f"{GREEN}{BOLD}🟢 Nuevo cliente{RESET}\n")
        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        email = input("Email: ").strip()
        if not (nombre and apellidos and email):
            print(f"{RED}⚠️  Todos los campos son obligatorios.{RESET}")
        else:
            cursor.execute("INSERT INTO clientes (nombre, apellidos, email) VALUES (?, ?, ?)", (nombre, apellidos, email))
            conexion.commit()
            print(f"{GREEN}✔️ Cliente añadido correctamente.{RESET}")
        input(f"\n{GRAY}Presiona ENTER para continuar...{RESET}")

    # === LISTAR CLIENTES ===
    elif opcion == 2:
        limpiar()
        banner()
        print(f"{CYAN}{BOLD}📋 Clientes registrados:{RESET}\n")
        tabla_clientes()
        input(f"{GRAY}Presiona ENTER para volver...{RESET}")

    # === ACTUALIZAR ===
    elif opcion == 3:
        limpiar()
        banner()
        print(f"{YELLOW}{BOLD}✏️  Actualizar cliente{RESET}\n")
        tabla_clientes()
        identificador = input("ID del cliente a actualizar: ").strip()
        cursor.execute("SELECT * FROM clientes WHERE Identificador = ?", (identificador,))
        cliente = cursor.fetchone()
        if cliente:
            print(f"\nCliente actual: {cliente[1]} {cliente[2]} - {cliente[3]}")
            nombre = input("Nuevo nombre (ENTER = mantener): ").strip() or cliente[1]
            apellidos = input("Nuevos apellidos (ENTER = mantener): ").strip() or cliente[2]
            email = input("Nuevo email (ENTER = mantener): ").strip() or cliente[3]
            cursor.execute("UPDATE clientes SET nombre=?, apellidos=?, email=? WHERE Identificador=?",
                           (nombre, apellidos, email, identificador))
            conexion.commit()
            print(f"{GREEN}✔️ Cliente actualizado con éxito.{RESET}")
        else:
            print(f"{RED}❌ No existe ese ID.{RESET}")
        input(f"\n{GRAY}Presiona ENTER para continuar...{RESET}")

    # === ELIMINAR ===
    elif opcion == 4:
        limpiar()
        banner()
        print(f"{RED}{BOLD}❌ Eliminar cliente{RESET}\n")
        tabla_clientes()
        identificador = input("ID del cliente a eliminar: ").strip()
        cursor.execute("SELECT * FROM clientes WHERE Identificador = ?", (identificador,))
        cliente = cursor.fetchone()
        if cliente:
            confirmar = input(f"¿Eliminar a {cliente[1]} {cliente[2]}? (s/n): ").lower()
            if confirmar == "s":
                cursor.execute("DELETE FROM clientes WHERE Identificador = ?", (identificador,))
                conexion.commit()
                reenumerar_ids()
                print(f"{GREEN}🗑️ Eliminado y lista reenumerada.{RESET}")
            else:
                print(f"{YELLOW}↩️  Operación cancelada.{RESET}")
        else:
            print(f"{RED}⚠️  No se encontró el cliente.{RESET}")
        input(f"\n{GRAY}Presiona ENTER para continuar...{RESET}")

    # === SALIR ===
    elif opcion == 5:
        animacion_salida()
        conexion.close()
        break

    else:
        print(f"{RED}❌ Opción fuera de rango.{RESET}")
        time.sleep(1.2)


