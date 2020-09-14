#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
#Author: Emily Dougherty
#This is a program for an etch a sketch gamein which the user inputs
#the size of the board and controls where 'X's are drawn. the board 
#can be 'shaken' at any time to clear the game board

import sys
import numpy as np
import Adafruit_BBIO.GPIO as GPIO
import time

newcur_y = 1
newcur_x = 1
cur_x = 1
cur_y =1


#setting up the GPIO pins that the buttons are using
GPIO.setup("P9_11", GPIO.IN) #left
GPIO.setup("P9_13", GPIO.IN) #right
GPIO.setup("P9_23", GPIO.IN) #up 
GPIO.setup("P9_17", GPIO.IN) #down
GPIO.setup("P9_27", GPIO.IN) #clear
GPIO.setup("P9_24", GPIO.IN) #exit
#initilizing button events
GPIO.add_event_detect("P9_11", GPIO.FALLING)
GPIO.add_event_detect("P9_13", GPIO.FALLING)
GPIO.add_event_detect("P9_23", GPIO.FALLING)
GPIO.add_event_detect("P9_17", GPIO.FALLING)
GPIO.add_event_detect("P9_27", GPIO.FALLING)
GPIO.add_event_detect("P9_24", GPIO.FALLING)

print("Welcome to Etch-A-Sketch! To start playing simply enter the dimensions ",
    "of the board you wish to play on. Then you will be prompted which direction ",
    "you would like to move in by using the buttons. The | shows where you currently",
    "are. You can clear the board by pressing the clear button. If at any ",
    "point you wish to leave the game simply type 'exit'. Enjoy! \n")

#The user inputs the size of they board they want
x = int(input("Size of board in X direction \n"))
y = int(input("Size of board in Y direction \n"))

#an empty board is generated and then the grid numbers are added
etch = np.full((y,x), ' ')
print("\n")
for i in range(x):
    etch[0][i] = i
for j in range(y):
    etch[j][0] = j
    
#initialize the starting point of the cursor
etch[1][1] = '|'

print('\n' .join([''.join(['{:4}'.format(item) for item in row])
                for row in etch]))
print("you can move left, right, up, down, or shake to clear")

#This is the main loop the game is played in
while(1):


    temp = 1

    if temp == 1:
        
        if GPIO.event_detected("P9_11"): #each button has their own specific event
            if cur_x == 1: #edge detection & correction
                newcur_x = x-1
            else:
                newcur_x = cur_x - 1 #adjusting the coordinates of the cursor
            etch[newcur_y][newcur_x] = "|" #setting the cursor
            etch[cur_y][cur_x] = "X" #keeping track of where they have been
            cur_x=newcur_x #updating the cursor position
            cur_y=newcur_y
            print("moving left!")
            print('\n' .join([''.join(['{:4}'.format(item) for item in row])
                for row in etch])) #reprinting the updated board
        elif GPIO.event_detected("P9_13"): #the next three events foloow the same pattern as above
            if cur_x == x-1:
                newcur_x = 1
            else:
                newcur_x = cur_x + 1
            etch[newcur_y][newcur_x] = "|"
            etch[cur_y][cur_x] = "X"
            cur_x=newcur_x
            cur_y=newcur_y
            print("moving right!")
            print('\n' .join([''.join(['{:4}'.format(item) for item in row])
                for row in etch]))
        elif GPIO.event_detected("P9_23"):
            if cur_y == 1:
                newcur_y = y-1
            else:
                newcur_y = cur_y - 1
            etch[newcur_y][newcur_x] = "|"
            etch[cur_y][cur_x] = "X"
            cur_x=newcur_x
            cur_y=newcur_y
            print("moving up!")
            print('\n' .join([''.join(['{:4}'.format(item) for item in row])
                for row in etch]))
        elif GPIO.event_detected("P9_17"):
            if cur_y == y-1:
                newcur_y = 1
            else:
                newcur_y = cur_y + 1
            etch[newcur_y][newcur_x] = "|"
            etch[cur_y][cur_x] = "X"
            cur_x=newcur_x
            cur_y=newcur_y
            print("moving down!")
            print('\n' .join([''.join(['{:4}'.format(item) for item in row])
                for row in etch]))
        elif GPIO.event_detected("P9_27"): #this is the clear button
            etch = np.full((y,x), ' ') #clears the board and keeps the cursor in the same position
            for i in range(x):
                etch[0][i] = i
            for j in range(y):
                etch[j][0] = j
            etch[cur_y][cur_x] = '|'
            print('\n' .join([''.join(['{:4}'.format(item) for item in row])
                for row in etch]))
        elif GPIO.event_detected("P9_24"): #exit button
            break

    
    


