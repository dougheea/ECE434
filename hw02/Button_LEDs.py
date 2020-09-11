#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
import Adafruit_BBIO.GPIO as GPIO
import time
GPIO.setup("P9_12", GPIO.OUT)
GPIO.setup("P9_14", GPIO.OUT)
GPIO.setup("P9_16", GPIO.OUT)
GPIO.setup("P9_18", GPIO.OUT)

GPIO.setup("P9_11", GPIO.IN)
GPIO.setup("P9_13", GPIO.IN)
GPIO.setup("P9_15", GPIO.IN)
GPIO.setup("P9_17", GPIO.IN)

count1 = 0
count2 = 0
count3 = 0
count4 = 0

while(1):
    if GPIO.input("P9_11"):
        if count1 ==0:
            time.sleep(0.5)
            GPIO.output("P9_12", GPIO.HIGH)
            count1 += 1
        else:
            time.sleep(0.5)
            GPIO.output("P9_12", GPIO.LOW)
            count1 -= 1
    if GPIO.input("P9_13"):
        if count2 ==0:
            time.sleep(0.5)
            GPIO.output("P9_14", GPIO.HIGH)
            count2 += 1
        else:
            time.sleep(0.5)
            GPIO.output("P9_14", GPIO.LOW)
            count2 -=1
    if GPIO.input("P9_15",):
        if count3 ==0:
            time.sleep(0.5)
            GPIO.output("P9_16", GPIO.HIGH)
            count3 +=1
        else:
            time.sleep(0.5)
            GPIO.output("P9_16", GPIO.LOW)
            count3 -= 1
    if GPIO.input("P9_17"):
        if count4 ==0:
            time.sleep(0.5)
            GPIO.output("P9_18", GPIO.HIGH)
            count4 +=1
        else:
            time.sleep(0.5)
            GPIO.output("P9_18", GPIO.LOW)
            count4 -=1

GPIO.cleanup()