#!/usr/bin/env python3
#chmod +x etch_a_sketch.py
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P9_12", GPIO.OUT)
GPIO.output("P9_12", GPIO.LOW)
sleep(1)
GPIO.output("P9_12", GPIO.HIGH)

GPIO.cleanup()