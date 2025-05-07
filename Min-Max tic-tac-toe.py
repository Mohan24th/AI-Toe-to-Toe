# Creates and returns a 3x3 empty board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]#this can be made more simple using just for loop

# Prints the current board with row and column numbers
def print_board(board):
    print("\n    1   2   3")
    print("  +---+---+---+")
    for i, row in enumerate(board):
        print(f"{i+1} | {' | '.join(row)} |")# can remove enumerate and wrute using simple for loop
        print("  +---+---+---+")
    print()

# Checks if the given player ('X' or 'O') has won
def check_winner(board, player):
    for i in range(3):
        # Check each row and column
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    # Check both diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Checks if the board is completely filled
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Evaluates the board and returns score
# +1 for AI win, -1 for Human win, 0 for draw or unfinished
def evaluate(board):
    if check_winner(board, "O"):
        return 1  # AI wins
    elif check_winner(board, "X"):
        return -1  # Human wins
    else:
        return 0  # No winner (yet)

# Minimax algorithm to calculate the best move
# is_maximizing: True if it's AI's turn, False for human
def minimax(board, is_maximizing):
    # Base case: check terminal state and return evaluated score
    if check_winner(board, "O") or check_winner(board, "X") or is_board_full(board):
        return evaluate(board)

    if is_maximizing:
        # AI is trying to maximize its score
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"  # Try AI move
                    score = minimax(board, False)  # Recurse for human's move
                    board[i][j] = " "  # Undo move
                    best_score = max(best_score, score)
        return best_score
    else:
        # Human is minimizing the AI's score
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"  # Try human move
                    score = minimax(board, True)  # Recurse for AI's move
                    board[i][j] = " "  # Undo move
                    best_score = min(best_score, score)
        return best_score

# Uses minimax to find the best move for AI
def get_best_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"  # Try a move
                score = minimax(board, False)  # Simulate outcome
                board[i][j] = " "  # Undo move
                if score > best_score:
                    best_score = score
                    best_move = (i, j)  # Store best move found
    return best_move

# Gets and validates human move input
def get_human_move(board):
    while True:
        try:
            move = input(" Your move (row,col): ")
            row, col = map(int, move.strip().split(','))
            row -= 1
            col -= 1
            if row in range(3) and col in range(3):
                if board[row][col] == " ":
                    return row, col
                else:
                    print(" That cell is already taken.")
            else:
                print(" Enter numbers from 1 to 3.")
        except ValueError:
            print(" Please use the format row,col (e.g., 2,3).")

# Main function to run the game
def play_game():
    board = create_board()
    print(" Welcome to Tic Tac Toe!")
    print("You are X, AI is O")
    print_board(board)

    while True:
        # Human move
        row, col = get_human_move(board)
        board[row][col] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print(" You win!")
            break
        if is_board_full(board):
            print(" It's a draw!")
            break

        # AI move
        print(" AI is thinking...")
        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print(" AI wins!")
            break
        if is_board_full(board):
            print(" It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
