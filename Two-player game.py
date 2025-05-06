def create_board(): #creates a 3D grid
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):#print the board/grid
    print("\n    1   2   3")
    print("  +---+---+---+")
    for i, row in enumerate(board):
        row_str = f"{i+1} | " + " | ".join(row) + " |"
        print(row_str)
        print("  +---+---+---+")
    print()

def check_winner(board, player): #checks if the player has won
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):#row
            return True
        if all(board[j][i] == player for j in range(3)):#colmun
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):#main diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):#top right to bottom left
        return True
    return False

def is_board_full(board):#checks if the board is full for draw condition
    return all(cell != " " for row in board for cell in row)

def get_move(player, board): #gets the move from the player which are valid 
    while True:
        try:
            move = input(f"Player {player}, enter your move as row,col (e.g., 1,3): ")
            row, col = map(int, move.strip().split(','))
            row -= 1
            col -= 1
            if row in range(3) and col in range(3):
                if board[row][col] == " ":
                    return row, col
                else:
                    print(" That cell is already occupied. Try again.")   #conditions for valid inputs
            else:
                print(" Invalid row/column. Please choose from 1 to 3.")
        except ValueError:
            print(" Invalid input format. Use row,col like 2,3")

def play_game():# main block where the above functions are called 
    board = create_board()
    current_player = "X"

    print(" Welcome to Tic Tac Toe!\n")
    print_board(board)

    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f" Player {current_player} wins!")
            break

        if is_board_full(board):
            print(" It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":  
    play_game()
