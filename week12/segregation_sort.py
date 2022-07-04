# 1. Name:
#      Mark Van Horn
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      This program will sort a list of numbers using the segregation sort algorithm.
#      It picks an element as pivot and partitions the given array around the picked pivot.
# 4. What was the hardest part? Be as specific as possible.
#      Getting the segregate function to work correctly. The pseudocode didn't quite work,
#      so I had to look at the code and figure out how to make it work.
# 5. How long did it take for you to complete the assignment?
#      1.5 hours

import random
import time

######################################
# Sort function: Initializes the     #
# recursive sort function.           #
######################################
def sort(array):
    return sort_recursive(array, 0, len(array) - 1)

######################################
# Segregate function: Partitions the #
# given array around the pivot.      #
######################################
def segregate(array, i_begin, i_end):
    i_pivot, partition = array[i_end], i_begin
    for i in range(i_begin, i_end):
        if array[i] <= i_pivot:
            array[i], array[partition] = array[partition], array[i]
            partition += 1

    array[partition], array[i_end] = array[i_end], array[partition]
    return partition

######################################
# Sort_recursive function:           #
# Recursively sorts the given array  #
# around the pivot.                  #
######################################
def sort_recursive(array, i_begin, i_end):
    if len(array) == 1:
        return array
    if i_begin < i_end:
        i_pivot = segregate(array, i_begin, i_end)
        sort_recursive(array, i_begin, i_pivot -  1)
        sort_recursive(array, i_pivot + 1, i_end)
    return array
	
######################################
# Handle function: Prints the        #
# unsorted list, sorts the list,     #
# and prints the sorted list.        #
######################################
def handle(array):
    if len(array) > 0:
        print(f"Unsorted list: {array}")
        array = sort(array)
        print(f"Sorted list: {array}")
    else:
        print(f"Unsorted list: {array}")
        print("The list is empty.")

######################################
# Main function: Calls the handle    #
# function. Also holds the test      #
# cases for the testing mode.        #
######################################
def main():
    mode = input("Enter 's' for standard mode or 't' for test mode: ")
    if mode == 's':
        arr = list(input("Enter a list of numbers separated by spaces: ").split())
        handle(arr)
    elif mode == 't':

        ######################################
        # Test 1: Empty list                 #
        ######################################
        time.sleep(0.5)
        print("\nTest 1: Empty list")
        arr = []
        handle(arr)

        ######################################
        # Test 2: List of identical elements #
        ######################################
        time.sleep(0.5)
        print("\nTest 2: List of one number")
        arr = [1,1,1,1]
        handle(arr)

        ######################################
        # Test 3: List of one element        #
        ######################################
        time.sleep(0.5)
        print("\nTest 3: Single element list")
        arr = [1]
        handle(arr)

        ######################################
        # Test 4: List in reverse order      #
        ######################################
        time.sleep(0.5)
        print("\nTest 4: Reverse sorted list")
        arr = [4,3,2,1]
        handle(arr)

        ######################################
        # Test 5: List of strings            #
        ######################################
        time.sleep(0.5)
        print("\nTest 5: List of strings")
        arr = ["yes", "no", "maybe", "so"]
        handle(arr)

        ######################################
        # Test 6: List of boolean values     #
        ######################################
        time.sleep(0.5)
        print("\nTest 6: List of boolean values")
        arr = [True, False, True, False]
        handle(arr)

        ######################################
        # Test 7: List of random numbers     #
        ######################################
        time.sleep(0.5)
        print("\nTest 7: List of mixed values")
        arr = [random.randint(0, 1000) for i in range(20)]
        handle(arr)

        ######################################
        # Test 8: List of random numbers     #
        ######################################
        time.sleep(0.5)
        print("\nTest 8: List of mixed values")
        arr = [9,6,3,8,6,4,3,2,66,6,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0]
        handle(arr)

        print()

main()