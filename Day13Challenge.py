# Write a program to shuffle the elements of a list randomly.

from random import shuffle
from copy import deepcopy

def get_values(n):
    lstValues = []
    for _ in range(n):
        lstValues.append((input("Please enter the value to be added to the list: ")))
    return lstValues
    
if __name__ == "__main__":
    x = input("Enter the number of elements in the list: ")
    try:
        n = int(x)
        lstValues = get_values(n)
        originalList = deepcopy(lstValues)
        shuffle(originalList)

        print("Original List is: {}. \nRandomlly shuffled list is: {}.".format(lstValues,originalList))
    except ValueError:
        print("Please enter valid number!")
    