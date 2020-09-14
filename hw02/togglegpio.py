#!/usr/bin/env python3
#chmod +x togglegpio.py
import Adafruit_BBIO.GPIO as GPIO
import time
GPIO.setup("P9_12", GPIO.OUT)

while(1):
    GPIO.output("P9_12", GPIO.HIGH)
    time.sleep(0.005)
    GPIO.output("P9_12", GPIO.LOW)
    time.sleep(0.005)