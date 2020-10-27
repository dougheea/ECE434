#!/usr/bin/env python3
import blynklib
import blynktimer
import sys
import os

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

@blynk.handle_event('write V0')
def allIWantForChristmas(pin, value):
    print("Playing Mariah Carey's 'All I Want For Christmas is You'")
    os.system("mplayer -ao alsa:device=sysdefault=Set AllIWantForChristmas.mp3")
    
while True:
    blynk.run()
   