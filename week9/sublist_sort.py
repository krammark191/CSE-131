# 1. Name:
#      Mark Van Horn
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This program will sort a list by using a sub-list. The program will
#      read a list of numbers from a file and sort the list by using a sub-
#      list. The program will then write the sorted list to a file. The sorting
#      will work by traversing the list and creating two sub-lists from sorted
#      sections from the original list. The sub-lists will be sorted by using
#      the same method as the original list. The sub-lists will then be
#      merged back together to create a sorted list.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

def main():
    """
    This function will run the program.
    """
    file = get_file() # get the file
    list = get_list(file) # get the list
    print(list) # print the list
    create_sub_lists(list) # create the sub-lists
    print(list) # print the sorted list
    file.close() # close the file
    pass

def get_file():
    """
    This function will get the file name from the user.
    Then it will open the file and read the contents.
    """
    file_name = input("Enter the file name: ") # get the file name from the user
    try: # try to open the file
        file = open(file_name, "r") # open the file
    except FileNotFoundError: # if the file is not found
        print("File not found.") # print error message
        return get_file() # call the function again
    return file # return the file

def get_list(file):
    """
    This function will get the list from the file.
    """
    list = [] # create an empty list
    for line in file: # for each line in the file
        list.append(int(line)) # append the line to the list
    return list # return the list

def create_sub_lists(list):
    """
    This function will create two sub-lists.
    """
    sub_list_1 = 0 # create an empty sub-list index
    sub_list_2 = 0 # create an empty sub-list index
    return list