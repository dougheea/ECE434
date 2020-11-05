#!/usr/bin/env python3
import blynklib
import blynktimer
import sys
import os
import logging
import threading
import time
import ctypes
import subprocess

# Get the authorization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
global pid

player = subprocess.Popen(["mplayer", "-quiet", "hozier.mp3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


time.sleep(10)
#player.stdin.write("q")
player.communicate(b"q")

def song1Lights():
    print("Playing Mariah Carey's 'All I Want For Christmas is You'")
    pid = os.getpid()
    print(pid)
    os.system("mplayer -ao alsa:device=sysdefault=Set hozier.mp3")
    
    print("finished playing")


#@blynk.handle_event('write V0')
def song1():
    print("BLINKY BLINKY TIME")
    time.sleep(60)
    print("finished 60 sec")
    time.sleep(120)
    print("finished 3 min")
    
#@blynk.handle_event('write V1')
def stop():
    print("MADE IT")
    print(pid)
    os.kill(pid)
    
        

    
#if __name__ == "__main__":
    #testThread = threading.Thread(target=song1Lights)
    #testThread.start()
    #while(1):
      #  temp = sys.argv
     #   if(temp == )

    #print("all done")
   
   