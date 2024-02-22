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
    sheep = None
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
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
        
tries = 1
explored = []
points = 0
touched_ships = {"2A": [], "2B": [], "3A": [], "4A": [], "5A": []}
board = generate_board()

def show_user_table(explored, board):
    for row in range(10):
        for column in range(10):
            if (row,column) in explored:
                if board[row][column] == EMPTY:
                    print(f'{WATER:2s}', end='')
                elif board[row][column] == TOUCHED:
                    print(f'{TOUCHED:2s}', end='')
                else:
                    print(f'{SUNKEN:2s}', end='')
            else:
                print(f'{UNEXPLORED:2s}', end='')
        print()

def process_target(target, board):
    global points
    if board[target[0]][target[1]] == EMPTY:
        if points > 0: points -= 1
        print(f"*****¡Agua!***** Puntos: {points}")
    else:
        ship_str = board[target[0]][target[1]]
        touched_ships[ship_str].append(target)
        if len(touched_ships[ship_str]) == int(ship_str[0]):
            points += 4 * int(ship_str[0])
            for ship in touched_ships[ship_str]: board[ship[0]][ship[1]] = SUNKEN
            print(f"*****¡Tocado y hundido!***** Puntos: {points}")
        else:
            points += 2 * int(ship_str[0])
            board[target[0]][target[1]] = TOUCHED
            print(f"*****¡Tocado!***** Puntos: {points}")

def is_over(board: list[list[str]]) -> bool:
    for row in board:
        for item in row:
            if item != WATER and item != TOUCHED and item != SUNKEN and item != UNEXPLORED and item != EMPTY:
                return False
    return True

############ MAIN LOOP ############

while True:
    if is_over(board): break
    print(f"------------ Intento {tries} ------------")
    target_raw = input("Introduzca la posición de tiro (enemigo): ")
    target = (ord(target_raw[0]) - 65, int(target_raw[1:]) - 1)
    if target in explored or target[0] not in range(10) or target[1] not in range(10):
      print("Posición ya explorada o inválida.")
      continue
    explored.append(target)
    process_target(target, board)
    show_user_table(explored, board)
    tries += 1
print("Se acabó, has destruido a delki, GG WP")
 



 