#!/usr/bin/env python3
# From: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
'''
	Raspberry Pi GPIO Status and Control
'''
import sys
import numpy as np
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
import os
import blynklib
import blynktimer

global newcur_x
global newcur_y
global cur_x
global cur_y
global lightboard

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
# create timers dispatcher instance
timer = blynktimer.Timer()



print("Welcome to Etch-A-Sketch! To start playing simply enter the dimensions ",
    "of the board you wish to play on. Then you will be prompted which direction ",
    "you would like to move in by using the buttons. The | shows where you currently",
    "are. You can clear the board by pressing the clear button. Enjoy! \n")

x =8
y =9
#an empty board is generated
lightboard = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]



print("you can move left, right, up, down, or shake to clear")

newcur_y =1
newcur_x = 0
cur_x = 0
cur_y =1
lightboard[cur_x*2] = 0x80 #initalize starting position of cursor
bus.write_i2c_block_data(matrix, 0, lightboard) #sets the lights on the matrix
print(cur_x)
    
@blynk.handle_event('write V0')
def move_left(pin, value):
    global newcur_x
    global newcur_y
    global cur_x
    global cur_y
    global lightboard
    
    if cur_x == 0: #edge detection & correction
        newcur_x = x-1
    else:
        newcur_x = cur_x - 1 #adjusting the coordinates of the cursor
        
    cur_x=newcur_x #updating the cursor position
    cur_y=newcur_y
    lightboard[2*cur_x]=lightboard[2*cur_x] | (1<<(8-cur_y)) #uses bit shiftingto find the right row to light up
    bus.write_i2c_block_data(matrix, 0, lightboard) #lights up the designat0000000ed LED green
    print("moving left!")
    
        
@blynk.handle_event('write V1')
def move_right(pin, value):
    global newcur_x
    global newcur_y
    global cur_x
    global cur_y
    global lightboard
    
    if cur_x == x-1:
        newcur_x = 0
    else:
        newcur_x = cur_x + 1
        cur_x=newcur_x
        cur_y=newcur_y
        
        lightboard[2*cur_x]=lightboard[2*cur_x] | (1<<(8-cur_y))
        bus.write_i2c_block_data(matrix, 0, lightboard)
        print("moving right!")
        
    
@blynk.handle_event('write V2')
def move_up(pin, value):
    global newcur_x
    global newcur_y
    global cur_x
    global cur_y
    global lightboard
    
    if cur_y == 1:
        newcur_y = y-1
    else:
        newcur_y = cur_y - 1
        cur_x=newcur_x
        cur_y=newcur_y
        lightboard[2*cur_x]=lightboard[2*cur_x] | (1<<(8-cur_y))
        bus.write_i2c_block_data(matrix, 0, lightboard)
        print("moving up!")
        
        
@blynk.handle_event('write V3')
def move_down(pin, value):
    global newcur_x
    global newcur_y
    global cur_x
    global cur_y
    global lightboard
    
    if cur_y == y-1:
        newcur_y = 1
    else:
        newcur_y = cur_y + 1
        cur_x=newcur_x
        cur_y=newcur_y
        lightboard[2*newcur_x]=lightboard[2*newcur_x] | (1<<(8-newcur_y))
        bus.write_i2c_block_data(matrix, 0, lightboard)
        print("moving down!")
        
@blynk.handle_event('write V4')
def clear(pin, value):
    global newcur_x
    global newcur_y
    global cur_x
    global cur_y
    global lightboard
    
    lightboard= [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    lightboard[2*cur_x]=lightboard[2*cur_x] | (1<<(8-cur_y)) #keeps cursor where it was
    bus.write_i2c_block_data(matrix, 0, lightboard)
    print("clearing the board!")   
        
    #return render_template('index3.html') #write the info to the page
    
while True:
    blynk.run()
    time.sleep(0.2)