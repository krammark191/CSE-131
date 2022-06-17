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
#      The assignment was actually quite simple, but the hardest part was
#      figuring out how to sort the sub-lists.
# 5. How long did it take for you to complete the assignment?
#      About 1 hour.

import random
import time

def combine(source, destination, begin1, begin2, end2):
    end1 = begin2
    for i in range(begin1, end2):
        if begin1 < end1 and (begin2 == end2 or source[begin1] < source[begin2]):
            destination[i] = source[begin1]
            begin1 += 1
        else:
            destination[i] = source[begin2]
            begin2 += 1
    return destination

def sort(array):
    size = len(array)
    src = array
    des = [None for i in range(len(array))]
    num = 2

    while num > 1:
        num = 0
        begin1 = 0

        while begin1 < size:
            end1 = begin1 + 1
            while end1 < size and src[end1 - 1] <= src[end1]:
                end1 += 1
            
            begin2 = end1
            if begin2 < size:
                end2 = begin2 + 1
            else:
                end2 = begin2
            while end2 < size and src[end2 - 1] <= src[end2]:
                end2 += 1
            
            num += 1
            combine(src, des, begin1, begin2, end2)
            begin1 = end2
        temp = src
        src = des
        des = temp
    return src

def handle(array):
    if len(array) > 0:
        print(f"Unsorted list: {array}")
        array = sort(array)
        print(f"Sorted list: {array}")
    else:
        print(f"Unsorted list: {array}")
        print("The list is empty.")


def main():
    mode = input("Enter 's' for standard mode or 't' for test mode: ")
    if mode == 's':
        arr = list(input("Enter a list of numbers separated by spaces: ").split())
        handle(arr)
    elif mode == 't':
        time.sleep(0.5)
        print("\nTest 1: Empty list")
        arr = []
        handle(arr)
        time.sleep(0.5)
        print("\nTest 2: List of one number")
        arr = [1,1,1,1]
        handle(arr)
        time.sleep(0.5)
        print("\nTest 3: Single element list")
        arr = [1]
        handle(arr)
        time.sleep(0.5)
        print("\nTest 4: Reverse sorted list")
        arr = [4,3,2,1]
        handle(arr)
        time.sleep(0.5)
        print("\nTest 5: List of strings")
        arr = ["yes", "no", "maybe", "so"]
        handle(arr)
        time.sleep(0.5)
        print("\nTest 6: List of boolean values")
        arr = [True, False, True, False]
        handle(arr)
        time.sleep(0.5)
        print("\nTest 7: List of mixed values")
        arr = [random.randint(0, 1000) for i in range(20)]
        handle(arr)
        time.sleep(0.5)
        print("\nTest 8: List of mixed values")
        arr = [9,6,3,8,6,4,3,2,66,6,4,3,2,1,0,9,8,7,6,5,4,3,2,1,0]
        handle(arr)
        print()

main()