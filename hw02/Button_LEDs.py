#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
import Adafruit_BBIO.GPIO as GPIO
import time
GPIO.setup("P9_12", GPIO.OUT)
GPIO.output("P9_12", GPIO.LOW)
time.sleep(2)
GPIO.output("P9_12", GPIO.HIGH)

GPIO.cleanup()