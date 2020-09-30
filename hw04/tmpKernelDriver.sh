#!/bin/bash

#This code assumes that the tmp101 sensor address is 0x49

echo tmp101 0x49 > new_device #add as a new device
cd /sys/class/i2c-adapter/i2c-2/2-0049/hwmon/hwmon0 #access the new device's directory
cat temp1_input #print the value

