import os 
import time 

def clear_screen(): 
    """ 
    Clear the terminal screen for a clean display. 
    This function works for both Windows and Unix-based systems. 
    """ 
    os.system('cls' if os.name == 'nt' else 'clear') 
    
def display_board(board): 
    """ 
    Display the current state of the game board with row and column labels. 
    The board is a 2D list with 3 rows and 3 columns. 
    Each cell can be 'X', 'O', or ' ' (empty). 
    """ 
    clear_screen() # Clear the screen before reprinting the board 
    print("  1   2   3") 
    for i, row in enumerate(board, start=1): 
        print(f"{i} " + " | ".join(row)) 
        if i < 3: 
            print(" " + "-" * 11) 
            
def player_input(board, player): 
    """ 
    Get input from the player and update the board. 
    'player' is either 'Player 1' or 'Player 2'. 
    """ 
    player_symbol = 'X' if player == 'Player 1' else 'O' 
    while True: 
        try: 
            # Ask the player for their move (row and column), indexed from 1 to 3 
            row, col = map(int, input(f"{player}, enter your move (row and column, 1-3) seperated by a space: ").split()) 
            # Adjust indexing to 0-based for internal board representation 
            row -= 1 
            col -= 1 
            # Check if the chosen cell is empty 
            if board[row][col] == " ": 
                # Update the board with the player's move 
                board[row][col] = player_symbol 
                break 
            else: 
                # Inform the player that the spot is taken 
                print("That spot is already taken. Try again.") 
        except (ValueError, IndexError): 
            # Handle invalid input, such as non-numeric input or out-of-range indexes 
            print("Invalid input. Please enter row and column as two numbers between 1 and 3, separated by a space.") 
            
def check_win(board, player_symbol): 
    """ 
    Check if the player has won the game. 
    'player_symbol' is either 'X' or 'O'. 
    Returns True if the player has won, False otherwise. 
    """ 
    # Check rows for a win 
    for row in board: 
        if all(s == player_symbol for s in row): 
            return True 
    # Check columns for a win 
    for col in range(3): 
        if all(board[row][col] == player_symbol for row in range(3)): 
            return True 
    # Check diagonals for a win 
    if all(board[i][i] == player_symbol for i in range(3)) or all(board[i][2 - i] == player_symbol for i in range(3)): 
        return True 
    return False 

def check_draw(board): 
    """ 
    Check if the game is a draw. 
    Returns True if all cells are filled and no player has won. 
    """ 
    # Return True if every cell is filled (none are empty) 
    return all(all(cell != " " for cell in row) for row in board) 

def tic_tac_toe(): 
    """ 
    Main function to run the Tic-Tac-Toe game. 
    Initializes the board and alternates turns between players until a win or draw. 
    """ 
    while True: 
        # Initialize the empty board 
        board = [[" " for _ in range(3)] for _ in range(3)] 
        # Start with Player 1 
        current_player = "Player 1" 
        
        while True: 
            # Display the current state of the board 
            display_board(board) 
            # Get the current player's move 
            player_input(board, current_player) 

            # Determine the current player's symbol 
            player_symbol = 'X' if current_player == 'Player 1' else 'O' 
            
            # Check if the current player has won 
            if check_win(board, player_symbol): 
                display_board(board) 
                print(f"{current_player} wins!") 
                break 
            # Check if the game is a draw 
            elif check_draw(board): 
                display_board(board) 
                print("It's a draw!") 
                break 
            
            # Switch players: 'Player 1' to 'Player 2' and 'Player 2' to 'Player 1' 
            current_player = "Player 2" if current_player == "Player 1" else "Player 1" 

        
            
        # Ask if players want to play again or quit 
        play_again = input("Do you want to play again? (yes/no): ").lower() 
        if play_again != 'yes':
            print("Thanks for playing!")
            time.sleep(5)
            break

# Start the game
tic_tac_toe()
