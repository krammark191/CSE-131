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
            print(f"\nLoading board from {file_name}", end="")
            time.sleep(0.5)
            print(".", end="")
            time.sleep(0.5)
            print(".", end="")
            time.sleep(0.5)
            print(".")
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
    board_dict = {"board":board}
    with open(file_name, 'w') as f:
        json.dump(board_dict, f)
    exit()

def get_input():
    user_choice = input("> ").lower()
    while not user_choice == 'e' and not user_choice == 'o' and not user_choice == 'q':
        print("Incorrect input, please enter a valid choice.\n")
        display_options()
        get_input()
    return user_choice

def process_input(user_choice, board):
    match user_choice:
        case 'e':
            return edit_square(board)
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

def edit_square(board):
    print("Please enter the coordinates of the square.")
    coords = list(input("> ").lower())
    coords = sort_coords(coords)
    while coords[0].isalpha() and coords[1].isalpha() or not coords[0].isalpha() and not coords[1].isalpha():
        print("Invalid coordinates, must contain at least one letter and one number.")
        coords = list(input("> ").lower())
        coords = sort_coords(coords)
    while ord(coords[0]) < 97 or ord(coords[0]) > 104 or ord(coords[1]) < 49 or ord(coords[1]) > 57:
        print("Coordinates are out of range, please enter valid coordinates.")
        coords = list(input("> ").lower())
        coords = sort_coords(coords)
    print(f"Enter the new value for square {''.join(coords).upper()}")
    new_value = int(input("> "))
    while new_value < 1 or new_value > 9:
        print("Value entered is out of range, please pick a number between 1 and 9.")
        new_value = int(input("> "))

    # Changes value on the board, no validity checking yet.
    board[ord(coords[1]) - 49][ord(coords[0]) - 97] = new_value

    return board

def check_valid():
    pass

def get_options(board):
    print("Process not yet implemented. Returning you to the menu.")
    time.sleep(1)
    print()
    display_options()
    process_input(get_input(), board)

def display_options():
    print("Please choose one of the options below:")
    print("\'E\'\tChoose a square to edit")
    print("\'O\'\tChoose a square to get options")
    print("\'Q\'\tSave and quit")
    print()

def main():
    board = get_file()
    while True:
        display(board)
        display_options()
        board = process_input(get_input(), board)

main()