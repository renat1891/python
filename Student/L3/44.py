board = ["", "", "", "", ""]



def print_board():
    line = "-------------"
    print(line)
    print(f"| {board[0]} | {board[1]} | {board[2]} | {board[3]} | {board[4]}")
    print(line)

def user_input():
    col=int(input("введіть комірку: ")) 
    if col == 0:
        exit()
    let=input("введіть що хочете покласти: ")
    board[col-1]=let

while True:
    print_board()
    user_input()