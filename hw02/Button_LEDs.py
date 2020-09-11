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

while(1):
    if GPIO.input("P9_11"):
        GPIO.output("P9_12", GPIO.HIGH)
    if GPIO.input("P9_13"):
        GPIO.output("P9_14", GPIO.HIGH)
    if GPIO.input("P9_15",):
        GPIO.output("P9_16", GPIO.HIGH)
    if GPIO.input("P9_17"):
        GPIO.output("P9_18", GPIO.HIGH)
    


GPIO.cleanup()