### Setup.sh
This file should be run before anything else in this folder. This file configures the eQEP pins and it sets the values used in the temperature sensor program.

### Etch_a_sketch_encoders.py
This program uses encoders instead of buttons to move the cursor around the LED Matrix. Like the LED_Matrix file, the exercises/displays/matrix8x8 program to set up the matrix must be run prior to running my program. 

### Etch_a_sketch_LED_Matrix.py
This program incorporates the LED matrix into the etch a sketch program. The program is run in python3. Communication is done through i2c. The only requirement is to run exercises/displays/matrix8x8 to set the matrix after each time it is powered off. 

### temp_sensor.py
This program takes the inputs from 2 temperature sensors. The alert pin is configured to go off if the temp goes above/below the THigh/TLow values. If this occurs the program will print "Threshold reached" and display the temperature from the sensor that reached the threshold.

### temp_sensor.sh
A shell file that uses 2 temp sensors to take the temperature of the room. Communication is done through i2c. The program outputs the temperature in Fahrenheit from both sensors.