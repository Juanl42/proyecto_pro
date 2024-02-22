import random
import string

EMPTY = ''

UNEXPLORED = '⬛'
WATER = '🟦'
TOUCHED = '🟧'
SUNKEN = '🟥'


def generate_board(
    size: int = 10,
    ships: tuple[tuple[int, int]] = ((5, 1), (4, 1), (3, 2), (2, 1)),
) -> list[list[str]]:
    board = [[EMPTY for _ in range(size)] for _ in range(size)]
    for sheep_size, num_ships in ships:
        placed_ships = 0
        while placed_ships < num_ships:
            sheep_id = f'{sheep_size}{string.ascii_uppercase[placed_ships]}'
            row, col = random.randint(0, size), random.randint(0, size)
            step = random.choice((-1, 1))
            row_step, col_step = (step, 0) if random.randint(0, 1) else (0, step)
            breadcrumbs = []
            for _ in range(sheep_size):
                try:
                    if not (0 <= row < size and 0 <= col < size):
                        raise IndexError()
                    if board[row][col] == EMPTY:
                        board[row][col] = sheep_id
                        breadcrumbs.append((row, col))
                    else:
                        raise IndexError()
                    row += row_step
                    col += col_step
                except IndexError:
                    # reset board
                    for bc in breadcrumbs:
                        board[bc[0]][bc[1]] = EMPTY
                    break
            else:
                placed_ships += 1

    return board


def show_board(board: list[list[str]]) -> None:
    for row in board:
        for item in row:
            print(f'[{item:2s}]', end='')
        print()


# TU CÓDIGO DESDE AQUÍ HACIA ABAJO
# ↓↓↓↓↓↓↓↓↓

board = generate_board()

# Iniciar el juego
score = 0
turns = 0

while any(any(cell != EMPTY and cell != TOUCHED for cell in row) for row in board):
    # Esto es para mostrar el tablero
    for row in board:
        for item in row:
            print(f'[{item:2s}]', end='')
        print()

    # Esto es para la puntuación
    print(f"Turno: {turns} | Puntación: {score}")

    # Pedir jugadas
    guess = input("Introduce posición:").upper()
    if len(guess) != 2 or guess[0] not in string.ascii_uppercase or not guess[1].isdigit():
        print(" Posicón no valida. Por favor, introduzca una posición válida.")
        continue

    row, col = ord(guess[0]) - ord('A'), int(guess[1]) - 1

    # como funciona el intento del jugador
    if board[row][col] == EMPTY:
        print("Agua! -1 punto")
        score = max(0, score - 1)
        board[row][col] = WATER
    elif board[row][col] == TOUCHED or board[row][col] == SUNKEN:
        print("Ya has tocado esta posición. Vuelve a intentarlo.")
    else:
        print("Tocado!")
        ship_id = board[row][col]
        board[row][col] = TOUCHED

    turns += 1

# Mostrar el tablero final
for row in board:
    for item in row:
        print(f'[{item:2s}]', end=" ")
    print()

# Mostrar la puntuación final
print(f"Turno: {turns} | Puntación: {score}")
print("Haz hundido todos los barcos")