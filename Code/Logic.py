
# Logic file to be imported into the main file. This will allow the game to function and will later be used train the AI.


# Imports

import random
import time

# create a function to initialize the game

def start_game():
    # declare an empty lsit then appending 4 lists each with 4 elements

    matrix = []

    for i in range (4):
        matrix.append([0] * 4)

    # print the controls for the user 


    print ("the commands are as follows : ")
    print ("up arrow key - moves the tiles up")
    print ("down arrow key - moves the tiles down")
    print ("left arrow key - moves the tiles left")
    print ("right arrow key - moves the tiles right")


    add_new_tile(matrix)
    return matrix


def add_new_tile(matrix):
    # function to add a new tile to a random empty space in the matrix


    r = random.randint(0, 3)
    c = random.randint(0, 3)


    while (matrix[r] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)


    matrix[r] = 2  