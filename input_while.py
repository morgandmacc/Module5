"""
Author: Morgan McCarley
Program: input_while.py

Prompts user for numeric input between 1 and 100.  prompt user until the input is in the correct range.
"""


if __name__ == '__main__':

    #declare a list variable
    my_list = []

    #prompt and get the user input
    my_input = float(input("Enter a number between 1 and 100:"))

    #while user input is not good (in range)
    while my_input < 1 or my_input > 100:
        #prompt user for good input
        my_input = float(input("Enter a number between 1 and 100:"))

    #store in list
    my_list.append(my_input)

    #print the list
    print(my_list)



