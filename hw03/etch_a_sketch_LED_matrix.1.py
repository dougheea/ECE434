#!/usr/bin/env python3
#chmod +x etch_a_sketch_LED_matrix.py
#Author: Emily Dougherty
# This is a program for an etch a sketch game in which the user 
# controls what part of the board lights up. The board 
# can be 'shaken' at any time by pressing the clear button. There is also
# a button to exit the game.

import sys
import numpy as np
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

newcur_y =1
newcur_x = 0
cur_x = 0
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

#
x =8
y =9
#an empty board is generated
lightboard = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    
lightboard[cur_x*2] = 0x80 #initalize starting position of cursor

bus.write_i2c_block_data(matrix, 0, lightboard) #sets the lights on the matrix

print("you can move left, right, up, down, or shake to clear")

#This is the main loop the game is played in
while(1):


    temp = 1

    if temp == 1:
        
        if GPIO.event_detected("P9_11"): #each button has their own specific event
            if cur_x == 0: #edge detection & correction
                newcur_x = x-1
            else:
                newcur_x = cur_x - 1 #adjusting the coordinates of the cursor

            cur_x=newcur_x #updating the cursor position
            cur_y=newcur_y
                
            lightboard[2*cur_x]=lightboard[2*cur_x] | (1<<(8-cur_y)) #uses bit shiftingto find the right row to light up
            bus.write_i2c_block_data(matrix, 0, lightboard) #lights up the designated LED green
            print("moving left!")

                
        elif GPIO.event_detected("P9_13"): #the next three events foloow the same pattern as above
            if cur_x == x-1:
                newcur_x = 0
            else:
                newcur_x = cur_x + 1

            cur_x=newcur_x
            cur_y=newcur_y
            
            lightboard[2*cur_x]=lightboard[2*cur_x] | (1<<(8-cur_y))    
            bus.write_i2c_block_data(matrix, 0, lightboard)
            print("moving right!")

                
        elif GPIO.event_detected("P9_23"):
            if cur_y == 1:
                newcur_y = y-1
            else:
                newcur_y = cur_y - 1
            cur_x=newcur_x
            cur_y=newcur_y
            
            lightboard[2*cur_x]=lightboard[2*cur_x] | (1<<(8-cur_y))    
            bus.write_i2c_block_data(matrix, 0, lightboard)
            print("moving up!")

                
        elif GPIO.event_detected("P9_17"):
            if cur_y == y-1:
                newcur_y = 1
            else:
                newcur_y = cur_y + 1
            cur_x=newcur_x
            cur_y=newcur_y
            
            lightboard[2*newcur_x]=lightboard[2*newcur_x] | (1<<(8-newcur_y))    
            bus.write_i2c_block_data(matrix, 0, lightboard)
            print("moving down!")

        elif GPIO.event_detected("P9_27"): #this is the clear button
            #clears the board and keeps the cursor in the same position
            lightboard= [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
            
            lightboard[2*cur_x]=lightboard[2*cur_x] | (1<<(8-cur_y)) 
            bus.write_i2c_block_data(matrix, 0, lightboard)
            print("clearing the board!")    
        
        elif GPIO.event_detected("P9_24"): #exit button
            break

    
    


