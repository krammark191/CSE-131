# 1. Name:
#      Mark Van Horn
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      This program is a sudoku puzzle game.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was keeping track of all the error-handling.
#      I initially had all of the error-handling in the edit_square()
#      function but that proved to be impractical and horrible
#      cohesion due to many other functions needing the same error-handling,
#      so I split the error-handling into separate functions that could
#      be easily referenced by any other function.
# 5. How long did it take for you to complete the assignment?
#      About 6-7 hours. I spent a lot of time on extra functionality beyond
#      the base requirements.
# 6. Extra Credit List
#      - Unchangeable read-only values from the original board.
#      - Input error-handling, at no point should the user be able
#        to crash the program based on their input.
#      - Menu in lieu of "enter coordinate or press 'q' to quit."
#      - Excellent (in my opinion) cohesion and coupling.


import json
import time


def display(board):
    # Prints the top index line.
    print("\n   A B C   D E F   G H I")
    for i in range(0, 9):
        print(f"{i+1}", end="  ")
        for j in range(0, 9):
            if board[i][j] == 0:
                print("", end=" ")
            else:
                print(abs(board[i][j]), end="")

            if j == 2 or j == 5:
                print(" | ", end="")
            elif j < 8:
                print(" ", end="")
            else:
                print()
        if i == 2 or i == 5:
            print("   ------+-------+------")
    print()


def check_board(board):
    for i in range(9):
        for j in range(9):
            return True if board[i][j] < 0 else False


def prep_board(board):
    for i in range(9):
        for j in range(9):
            board[i][j] *= -1
    prepped_board = [[board[j][i] for i in range(9)] for j in range(9)]
    return prepped_board


def get_file():
    file_name = input("\nPlease enter a file name: ")
    try:
        with open(file_name) as f:
            board = json.load(f)
            print(f"\nLoading board from {file_name}")
            time.sleep(1)
            print("Board loaded successfully.\n")
            return board['board'] if check_board(board["board"]) else prep_board(board["board"])
    except:
        print("File does not exist. You get the easy board.\n")
        with open("131.05.Easy.json") as f:
            board = json.load(f)
            return board['board']


def save_file(board):
    file_name = input("Please enter a file name: ")
    with open(file_name, 'w') as f:
        json.dump({"board": board}, f)
    exit()


def get_input():
    user_choice = input("> ").lower()
    while user_choice not in {'d', 'e', 'o', 'q'}:
        # not user_choice == 'e' and not user_choice == 'o' and not user_choice == 'q' and not user_choice == 'd':
        print("Incorrect input, please enter a valid choice.\n")
        display_options()
        user_choice = input("> ").lower()
    return user_choice


def process_input(user_choice, board):
    match user_choice:
        case 'd':
            display(board)
            return board
        case 'e':
            return edit_square(board)
        case 'o':
            return get_options(board)
        case 'q':
            save_file(board)


def sort_coords(coords):
    if not coords[0].isalpha():
        temp = coords[0]
        coords[0] = coords[1]
        coords[1] = temp
    return coords


def check_valid(board, coords, value):
    column = ord(coords[0]) - 97
    row = ord(coords[1]) - 49
    for r in range(9):
        if abs(board[r][column]) == value:
            return 1
    for c in range(9):
        if abs(board[row][c]) == value:
            return 2

    col_start = int(row / 3) * 3
    row_start = int(column / 3) * 3

    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if abs(board[j][i]) == value:
                return 3

    return 0


def is_filled(board, coords):
    return 0 if board[ord(coords[1]) - 49][ord(coords[0]) - 97] < 0 else 1 if board[ord(coords[1]) - 49][ord(coords[0]) - 97] > 0 else 2


def check_coord_errors(board, coords):
    if not len(coords) == 2:
        print("Coordinates must consist of two characters; one letter and one number.")
        return False
    coords = sort_coords(coords)
    if coords[0].isalpha() and coords[1].isalpha() or not coords[0].isalpha() and not coords[1].isalpha():
        print("Invalid coordinates, must contain at least one letter and one number.")
        return False
    if ord(coords[0]) < 97 or ord(coords[0]) > 104 or ord(coords[1]) < 49 or ord(coords[1]) > 57:
        print("Coordinates are out of range, please enter valid coordinates.")
        return False
    if is_filled(board, coords) == 0:
        print(
            f"Value {abs(board[ord(coords[1]) - 49][ord(coords[0]) - 97])} "
            f"in \'{''.join(coords).upper()}\' "
            f"is a read-only value and cannot be changed.")
        return False
    elif is_filled(board, coords) == 1:
        print(
            f"Value {abs(board[ord(coords[1]) - 49][ord(coords[0]) - 97])} "
            f"in \'{''.join(coords).upper()}\' "
            f"is a read-write value and can be changed.")
    return True


def check_value_errors(board, coords, new_value):
    try:
        new_value = int(new_value)
    except:
        print("Value must be an integer.")
        return False
    if new_value < 1 or new_value > 9:
        print("Value entered is out of range, please pick a number between 1 and 9.")
        return False
    match check_valid(board, coords, new_value):
        case 0:
            return True
        case 1:
            print(f"{new_value} is already in the column.")
            return False
        case 2:
            print(f"{new_value} is already in the row.")
            return False
        case 3:
            print(f"{new_value} is already in the square.")
            return False
    return True


def get_coords(board):
    coords = list(
        input("Please enter the coordinates of the square.\n> ").lower())
    return sort_coords(coords) if check_coord_errors(board, coords) else get_coords(board)


def get_value(board, coords):
    new_value = input(
        f"Enter the new value for square {''.join(coords).upper()}\n> ")
    return int(new_value) if check_value_errors(board, coords, new_value) else get_value(board, coords)


def edit_square(board):
    coords = get_coords(board)
    new_value = get_value(board, coords)
    board[ord(coords[1]) - 49][ord(coords[0]) - 97] = new_value
    return board


def get_options(board):
    coords = get_coords(board)
    temp_value = board[ord(coords[1]) - 49][ord(coords[0]) - 97]
    board[ord(coords[1]) - 49][ord(coords[0]) - 97] = 0
    valid_options = []
    for i in range(1, 10):
        if check_valid(board, coords, i) == 0:
            valid_options.append(i)
    print(
        f"\nThe valid options for \'{''.join(coords).upper()}\' are: ", end="")
    print(*valid_options, sep=", ", end="\n\n")
    board[ord(coords[1]) - 49][ord(coords[0]) - 97] = temp_value
    return board
    # display_options()
    # process_input(get_input(), board)


def display_options():
    print("Please choose one of the options below:")
    print("\'D\'\tDisplay the board")
    print("\'E\'\tChoose a square to edit")
    print("\'O\'\tChoose a square to get options")
    print("\'Q\'\tSave and quit\n")


def main():
    board = get_file()
    while True:
        display(board)
        display_options()
        board = process_input(get_input(), board)


main()
