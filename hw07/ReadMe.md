### setup.sh
This file is used in the Blynk files. It's primary purpose is to set the authorization key. Note: before running it, make sure to source this file, otherwise the Blynk app will not pick it up.

### leds.py
This file uses Blynk to turn on the usr3 LED. It also can blink a virtual LED on the app by clicking a button on the breadboard. First run the python code and then start the application in Blynk.

### tempAndLED.py
This file uses Blynk to accomplish everything in leds.py and also reads a tmp101 sensor. The temperature will print out whenever a change occurs.