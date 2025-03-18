#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while not check_winner(board) and not is_board_full(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            # Check if the row and column are within bounds
            if row not in range(3) or col not in range(3):
                print("Invalid input. Row and column must be between 0 and 2. Try again.")
                continue
            
            if board[row][col] == " ":
                board[row][col] = player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter integers for row and column.")

    print_board(board)

    if check_winner(board):
        # Determine the actual winner (the last player who moved before the winning move)
        if player == "X":
            winner = "O"
        else:
            winner = "X"
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

tic_tac_toe()

