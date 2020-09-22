#!/usr/bin/env python3
#chmod +x temp_sensor.py

import time
import smbus
bus = smbus.SMBus(2)  # Use i2c bus 2

sensor1 = 0x48
sensor2 = 0x49


while(1):
    temp = bus.read_byte_data(0x48,0)
    temp2 = bus.read_byte_data(0x49,0)

    print(temp)
    print(temp2)

    temp = temp*9/5 +32
    temp2 = temp2*9/5 +32

    print(temp)
    print(temp2)
    time.sleep(2)