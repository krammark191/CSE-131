# 1. Name:
#      Mark Van Horn
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      This program is a sudoku puzzle game.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-


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
                print(board[i][j], end="")
            
            if j == 2 or j == 5:
                print(" | ", end="")
            elif j < 8:
                print(" ", end="")
            else:
                print()
        if i == 2 or i == 5:
            print("   ------+-------+------")
    print()

def get_file():
    file_name = input("\nPlease enter a file name: ")
    try:
        with open(file_name) as f:
            board = json.load(f)
            print(f"\nLoading board from {file_name}")
            time.sleep(1)
            print("Board loaded successfully.\n")
            return board['board']
    except:
        print("File does not exist. You get the easy board.\n")
        with open("131.05.Easy.json") as f:
            board = json.load(f)
            return board['board']

def save_file(board):
    file_name = input("Please enter a file name: ")
    with open(file_name, 'w') as f:
        json.dump({"board":board}, f)
    exit()

def get_input():
    user_choice = input("> ").lower()
    while not user_choice == 'e' and not user_choice == 'o' and not user_choice == 'q':
        print("Incorrect input, please enter a valid choice.\n")
        display_options()
        user_choice = input("> ").lower()
    return user_choice

def process_input(user_choice, board):
    match user_choice:
        case 'e':
            return edit_square(board, 1)
        case 'o':
            get_options(board)
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
        if board[r][column] == value:
            return 1
    for c in range(9):
        if board[row][c] == value:
            return 2

    col_start = int(row / 3) * 3
    row_start = int(column / 3) * 3

    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[j][i] == value:
                return 3

    return 0

def is_filled(board, coords):
    return False if board[ord(coords[1]) - 49][ord(coords[0]) - 97] == 0 else True

def check_coord_errors(board, coords):
    if not len(coords) == 2:
        print("Coordinates must consist of two characters; one letter and one number.")
        return False
    elif coords[0].isalpha() and coords[1].isalpha() or not coords[0].isalpha() and not coords[1].isalpha():
        print("Invalid coordinates, must contain at least one letter and one number.")
        return False
    elif ord(coords[0]) < 97 or ord(coords[0]) > 104 or ord(coords[1]) < 49 or ord(coords[1]) > 57:
        print("Coordinates are out of range, please enter valid coordinates.")
        return False
    elif is_filled(board, coords):
        print(f"There is already a value in \'{''.join(coords).upper()}\', please choose another square.")
        return False
    else:
        return True

def check_value_errors(board, coords, new_value):
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
    coords = list(input("Please enter the coordinates of the square.\n> ").lower())
    return coords if check_coord_errors(board, coords) else get_coords(board)

def get_value(board, coords):
    new_value = int(input(f"Enter the new value for square {''.join(coords).upper()}\n> "))
    return new_value if check_value_errors(board, coords, new_value) else get_value(board, coords)

def edit_square(board):
    coords = get_coords(board)

    # while not len(coords) == 2:
    #     print("Coordinates must consist of one letter and one number.")
    #     coords = list(input("> ").lower())
    # coords = sort_coords(coords)

    # while coords[0].isalpha() and coords[1].isalpha() or not coords[0].isalpha() and not coords[1].isalpha():
    #     print("Invalid coordinates, must contain at least one letter and one number.")
    #     coords = list(input("> ").lower())
    #     while not len(coords) == 2:
    #         print("Coordinates must consist of one letter and one number.")
    #         coords = list(input("> ").lower())
    #     coords = sort_coords(coords)

    # while ord(coords[0]) < 97 or ord(coords[0]) > 104 or ord(coords[1]) < 49 or ord(coords[1]) > 57:
    #     print("Coordinates are out of range, please enter valid coordinates.")
    #     coords = list(input("> ").lower())
    #     while not len(coords) == 2:
    #         print("Coordinates must consist of one letter and one number.")
    #         coords = list(input("> ").lower())
    #     coords = sort_coords(coords)

    # if is_filled(board, coords):
    #     print(f"There is already a value in \'{''.join(coords).upper()}\', please choose another square.")
    #     edit_square(board, type)

    # Value input
    # if type == 2:
    #     return coords

    new_value = get_value(board, coords)

    # print(f"Enter the new value for square {''.join(coords).upper()}")
    # new_value = int(input("> "))

    # while new_value < 1 or new_value > 9:
    #     print("Value entered is out of range, please pick a number between 1 and 9.")
    #     new_value = int(input("> "))

    # while not check_valid(board, coords, new_value) == 0:
    #     match check_valid(board, coords, new_value):
    #         case 1:
    #             print(f"{new_value} is already in the column.")
    #         case 2:
    #             print(f"{new_value} is already in the row.")
    #         case 3:
    #             print(f"{new_value} is already in the square.")
    #     new_value = int(input("> "))

    board[ord(coords[1]) - 49][ord(coords[0]) - 97] = new_value

    return board

def get_options(board):
    coords = get_coords(board)
    # while is_filled(board, coords):
    #     print(f"There is already a value in \'{''.join(coords).upper()}\', please choose another square.")
    #     coords = get_coords()
    valid_options = []
    for i in range(1, 10):
        if check_valid(board, coords, i) == 0:
            valid_options.append(i)
    print(f"\nThe valid options for \'{''.join(coords).upper()}\' are: ", end="")
    print(*valid_options, sep=", ", end="\n\n")
    display_options()
    process_input(get_input(), board)

def display_options():
    print("Please choose one of the options below:")
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