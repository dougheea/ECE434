#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
#Author: Emily Dougherty
#This is a program for an etch a sketch gamein which the user inputs
#the size of the board and controls where 'X's are drawn. the board 
#can be 'shaken' at any time to clear the game board

import sys
import numpy as np
newcur_y = 1
newcur_x = 1
cur_x = 1
cur_y =1

print("Welcome to Etch-A-Sketch! To start playing simply enter the dimensions ",
    "of the board you wish to play on. Then you will be prompted which direction ",
    "you would like to move in. After moving, you can decide if you would like to ",
    "place an X on that spot. You can clear the board by typing 'shake' If at any ",
    "point you wish to leave the game simply type 'exit'. Enjoy! \n")

#The user inputs the size of they board they want
x = int(input("Size of board in X direction \n"))
y = int(input("Size of board in Y direction \n"))
etch = np.full((y,x), ' ')
print("\n")

#an empty board is generated and then the grid numbers are added
for i in range(x):
    etch[0][i] = i
for j in range(y):
    etch[j][0] = j
#initialize the starting point of the cursor
etch[1][1] = '|'

#This is the main loop the game is played in
while(1):

    #This prints out the game board
    print('\n' .join([''.join(['{:4}'.format(item) for item in row])
        for row in etch]))

    print("you can move left, right, up, down, or shake to clear")
    text = input("Where would you like to move? \n")

    #deciding what the user wanted to do
    if text == 'shake':
        etch = np.full((y,x), ' ')
        for i in range(x):
            etch[0][i] = i
        for j in range(y):
            etch[j][0] = j
        etch[cur_y][cur_x] = '|'
    elif text == 'exit':
        break
    else:
        #adjusting the coordinates of the cursor
        if text == 'left':
            newcur_x = cur_x - 1
        elif text == 'right':
            newcur_x = cur_x + 1
        elif text == 'up':
            newcur_y = cur_y - 1
        elif text == 'down':
            newcur_y = cur_y + 1
        else:
            print("we didn't understand that, so you will not move this round")

        ans = input("would you like to place an x in this spot? (y or n) \n")

        #placing an X if the user wants to
        if ans == 'y':
            etch[newcur_y][newcur_x] = "X"
        elif ans == 'n':
            if etch[newcur_y][newcur_x] == " ":    
                etch[newcur_y][newcur_x] = "|"
        elif text == 'exit':
            break
        else:
            print("sorry, we didn't understand that")
        if etch[cur_y][cur_x] == "|":
            etch[cur_y][cur_x] = " "

        #setting the current coordinates
        cur_x = newcur_x
        cur_y = newcur_y
    
    


