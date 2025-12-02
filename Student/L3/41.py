
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]


winning_combos = [
    [(0, 0), (0, 1), (0, 2)],  
    [(1, 0), (1, 1), (1, 2)],  
    [(2, 0), (2, 1), (2, 2)],  
    [(0, 0), (1, 0), (2, 0)],  
    [(0, 1), (1, 1), (2, 1)],  
    [(0, 2), (1, 2), (2, 2)],  
    [(0, 0), (1, 1), (2, 2)],  
    [(0, 2), (1, 1), (2, 0)]   
]

def print_board(b):
    print("# -------------")
    for row in b:
        print(f"# | {row[0]} | {row[1]} | {row[2]} |")
        print("# -------------")

def check_win(player):
    for combo in winning_combos:
        if all(board[r][c] == player for r, c in combo):
            return True
    return False

current_player = "X"

for turn in range(9):
    print_board(board)
    print(f"player {current_player}")

    r = int(input("input row: ")) - 1
    c = int(input("input column: ")) - 1

    if board[r][c] != " ":
        print("Cell is already taken")
        continue

    board[r][c] = current_player

    if check_win(current_player):
        print_board(board)
        print(f"Player {current_player} won")
        break

    current_player = "O" if current_player == "X" else "X"
else:
    print_board(board)
    print("draw")