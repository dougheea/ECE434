# hw07 grading

| Points      | Description |
| ----------- | ----------- |
|  2 | Project Template
|  2 | | Names
|  0 | | Executive Summary - *missing*
| 10 | Blynk - TMP101
|  4 | Blynk - Etch-a-sketch - extra
| 18 | **Total**

*My comments are in italics. --may*

### setup.sh
This file is used in the Blynk files. It's primary purpose is to set the authorization key. Note: before running it, make sure to source this file, otherwise the Blynk app will not pick it up.

### leds.py
This file uses Blynk to turn on the usr3 LED. It also can blink a virtual LED on the app by clicking a button on the breadboard. First run the python code and then start the application in Blynk.

### tempAndLED.py
This file uses Blynk to accomplish everything in leds.py and also reads a tmp101 sensor. The temperature will print out whenever a change occurs.

### etch_a_sketch_blynk
This file takes the etch a sketch program from earlier in the quarter and uses blink to light up the board. The setup.sh file must be sourced before use.