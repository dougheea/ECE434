#!/usr/bin/env python3
#chmod +x temp_sensor.py

#Run the setup.sh file before this one. This program reads 2 temperature sensors and prints out the current temp when 
#the alert is tripped. The alert is trippedwhen the temperature goes above/below the THigh/TLow
#threshold. 

import time
import smbus
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P9_25", GPIO.IN) #alert on sensor 1
GPIO.add_event_detect("P9_25", GPIO.BOTH)

GPIO.setup("P9_28", GPIO.IN) #alert on sensor 1
GPIO.add_event_detect("P9_28", GPIO.BOTH)


bus = smbus.SMBus(2)  # Use i2c bus 2

sensor1 = 0x48 #temp1
sensor2 = 0x49 #temp2

tempnum =1

while(1):
    if  GPIO.event_detected("P9_25"):
        
        print("Threshold reached on temp 1")
        temp = bus.read_byte_data(0x48,0) #reading the temp from the sensor thata activated the alert

        temp = temp*9/5 +32 #converting to celicus

        print(temp)
        
        time.sleep(2)
        
    if  GPIO.event_detected("P9_28"):
        
        print("Threshold reached on temp 2")
        temp2 = bus.read_byte_data(0x49,0)

        temp2 = temp2*9/5 +32

        print(temp2)
        time.sleep(2)