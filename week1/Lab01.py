# 1. Name:
#      Mark Van Horn
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json

# The characters used in the Tic-Tac-Toe board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    try:
        f = open(filename)
    except:
        print("File does not exist. You get a blank board.")
        return blank_board['board']
    data = json.load(f)
    return data['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    with open(filename, "w") as outfile:
        json.dump(board, outfile)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    sum1 = 0
    sum2 = 0
    for i in board:
        if i == X:
            sum1 += 1
        elif i == O:
            sum2 += 1
    
    if sum1 == sum2 or sum1 == 0:
        return True
    return False

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    while True:
        if is_x_turn(board):
            user_in = input("X> ")
            if user_in == 'q':
                return True
            if board[int(user_in - 1)] == BLANK:
                board[int(user_in - 1)] = X
                break
        else:
            user_in = input("O> ")
            if user_in == 'q':
                return True
            if board[int(user_in - 1)] == BLANK:
                board[int(user_in - 1)] = O
                break
        print("That space is already filled, please try another square.")
    return False

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False


def welcome():
    # These user-instructions are provided and do not need to be changed.
    print("\nEnter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
    print("where the following numbers correspond to the locations on the grid:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")
    print("The current board is:")

# The file read code, game loop code, and file close code goes here.
play_again = True
while play_again:
    answer = input("\nWould you like to play a new game or load a previous game? (new/load): ")
    if answer.lower() == 'new':
        board = blank_board["board"]
    else:
        board = read_board(input("What is the file name? "))
    welcome()
    while game_done:
        display_board(board)
        if play_game(board):
            filename = input("What is the file name? ")
            break
    
    play_again = True if input("Would you like to play again? ").lower() == 'yes' else False
print("Thank you for playing!")