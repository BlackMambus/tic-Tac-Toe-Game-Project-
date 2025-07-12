def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")


def check_win(board, player):
    """Checks if the given player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_tie(board):
    """Checks if the board is full (tie game)."""
    for row in board:
        if " " in row:
            return False  # There's an empty cell, so it's not a tie
    return True  # No empty cells, it's a tie


def tic_tac_toe():
    """Plays a game of Tic-Tac-Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]  # Initialize the board
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        print(f"Player {current_player}, it's your turn.")

        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))

                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Invalid input. Row and column must be between 0 and 2.")
                    continue

                if board[row][col] != " ":
                    print("That cell is already occupied. Try again.")
                    continue

                break  # Valid move, exit the inner loop

            except ValueError:
                print("Invalid input. Please enter numbers.")

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            game_over = True
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()


