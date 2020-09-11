#!/usr/bin/env python3
#chmod +x etch_a_sketch.py


import Adafruit_BBIO.GPIO as GPIO
import time
#setting up the LEDS as inputs and the buttons as outputs
GPIO.setup("P9_12", GPIO.OUT)
GPIO.setup("P9_14", GPIO.OUT)
GPIO.setup("P9_20", GPIO.OUT)
GPIO.setup("P9_18", GPIO.OUT)

GPIO.setup("P9_11", GPIO.IN)
GPIO.setup("P9_13", GPIO.IN)
GPIO.setup("P9_15", GPIO.IN)
GPIO.setup("P9_17", GPIO.IN)
#initating a count to keep track if the LED should be turned on or off
count1 = 0
count2 = 0
count3 = 0
count4 = 0

while(1):
    if GPIO.input("P9_11"): #if this button is triggered then the count is checked
        if count1 == 0: # count value of zero means the LED is currently off
            time.sleep(0.1) 
            GPIO.output("P9_12", GPIO.HIGH) #LED is turned on
            count1 += 1 #count is changed to reflect the state of LED
        else:
            time.sleep(0.1)
            GPIO.output("P9_12", GPIO.LOW) #LED is turned off
            count1 -= 1 #count is changed to reflect the state of LED
    if GPIO.input("P9_13"):
        if count2 ==0:
            time.sleep(0.1)
            GPIO.output("P9_20", GPIO.HIGH)
            count2 += 1
        else:
            time.sleep(0.1)
            GPIO.output("P9_20", GPIO.LOW)
            count2 -=1
    if GPIO.input("P9_15",):
        if count3 ==0:
            time.sleep(0.1)
            GPIO.output("P9_20", GPIO.HIGH)
            count3 +=1
        else:
            time.sleep(0.1)
            GPIO.output("P9_20", GPIO.LOW)
            count3 -= 1
    if GPIO.input("P9_17"):
        if count4 ==0:
            time.sleep(0.1)
            GPIO.output("P9_18", GPIO.HIGH)
            count4 +=1
        else:
            time.sleep(0.1)
            GPIO.output("P9_18", GPIO.LOW)
            count4 -=1

GPIO.cleanup()