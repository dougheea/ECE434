#!/usr/bin/env python3
# Blink read the temperature from a BMP085 and display it
import blynklib
import blynktimer
import os
import smbus
import Adafruit_BBIO.GPIO as GPIO

tempSensor = 0x49 #temp1

# Run setup.sh to create a new bmp085
#BMP085='/sys/class/i2c-adapter/i2c-2/2-0077/iio:device1/in_temp_input'

# Setup the LED
LED = 'USR3'
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 1) 

# Setup the button
button = 'P9_11'
GPIO.setup(button, GPIO.IN)

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
# create timers dispatcher instance
timer = blynktimer.Timer()

bus = smbus.SMBus(2)  # Use i2c bus 2

# Register Virtual Pins
# The V* says to response to all virtual pins
@blynk.handle_event('write V0')
def my_write_handler(pin, value):
    print('Current V{} value: {}'.format(pin, value))
    GPIO.output(LED, int(value[0])) 
    
# This calback is called everytime the button changes
# channel is the name of the pin that changed
def pushed(channel):
    # Read the current value of the input
    state = GPIO.input(channel)
    print('Edge detected on channel {}, value={}'.format(channel, state))
    # Write it out
    GPIO.output(LED, state)     # Physical LED
    blynk.virtual_write(9, 255*state)  # Virtual LED: 255 max brightness

# This is a non-blocking event 
GPIO.add_event_detect(button, GPIO.BOTH, callback=pushed) 


oldtemp = 0
# Code below: register a timer for different pins with different intervals
# run_once flag allows to run timers once or periodically
@timer.register(vpin_num=10, interval=0.5, run_once=False)
def write_to_virtual_pin(vpin_num=1):
    global oldtemp
    # Open the file with the temperature
        #f = open(BMP085, "r")
    temp=  bus.read_byte_data(0x49,0) #f.read()[:-1]     # Remove trailing new line
    # Convert from mC to C
    #temp = int(temp)/1000
    #f.close()
    # Only display if changed
    if(temp != oldtemp):
        print("Pin: V{} = '{}".format(vpin_num, str(temp)))
        # Send to blynk
        blynk.virtual_write(vpin_num, temp)
        oldtemp = temp

while True:
    blynk.run()
    timer.run()
