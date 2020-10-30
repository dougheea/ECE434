#!/usr/bin/env python3
import blynklib
import blynktimer
import sys
import os
import logging
import threading
import time

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)


def song1Lights():
    print("BLINKY BLINKY TIME")
    time.sleep(60)
    print("finished 60 sec")
    time.sleep(120)
    print("finished 3 min")


@blynk.handle_event('write V0')
def song1(pin, value):
    testThread = threading.Thread(target=song1Lights)
    testThread.start()
    print("Playing Mariah Carey's 'All I Want For Christmas is You'")
    os.system("mplayer -ao alsa:device=sysdefault=Set hozier.mp3")
    print("finished playing")
        

    
if __name__ == "__main__":
    while True:
        blynk.run()
    print("all done")
   
   