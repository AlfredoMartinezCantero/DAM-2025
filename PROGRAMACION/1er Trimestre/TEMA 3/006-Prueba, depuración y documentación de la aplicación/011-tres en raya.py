print("Tres en raya - 2 jugadores humanos")
print("(c) 2025 Alfredo Martínez Cantero")

jugador = 1
tablero = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def mostrar_tablero(tablero):
  print(f'{tablero[0]}|{tablero[1]}|{tablero[2]}')
  print('------')
  print(f'{tablero[3]}|{tablero[4]}|{tablero[5]}')
  print('------')
  print(f'{tablero[6]}|{tablero[7]}|{tablero[8]}')

def verificar_ganador(tablero):
  lineas_ganadoras = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
    [0, 4, 8], [2, 4, 6]              # diagonales
  ]
  for linea in lineas_ganadoras:
    if tablero[linea[0]] == tablero[linea[1]] == tablero[linea[2]]:
      if tablero[linea[0]] in ['X', 'O']:
        return tablero[linea[0]]
  return None

while True:
  mostrar_tablero(tablero)
  
  while True:
    try:
      tirada = int(input(f"Tirada del jugador {jugador} (1-9): "))
      if 1 <= tirada <= 9 and isinstance(tablero[tirada - 1], int):
        break
      print("Casilla inválida o ya ocupada.")
    except ValueError:
      print("Ingresa un número válido.")
  
  simbolo = "X" if jugador == 1 else "O"
  tablero[tirada - 1] = simbolo
  
  ganador = verificar_ganador(tablero)
  if ganador:
    mostrar_tablero(tablero)
    print(f"¡Jugador {jugador} ({ganador}) gana!")
    break
  
  if all(not isinstance(x, int) for x in tablero):
    mostrar_tablero(tablero)
    print("¡Empate!")
    break
  
  jugador = 2 if jugador == 1 else 1
