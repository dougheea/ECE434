#!/usr/bin/env python3
import time
import subprocess
import shlex
import sys
import os
import signal
import blynklib
import blynktimer


# Get the authorization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

global stopState
stopState = False

@blynk.handle_event('write V0')
def playSong1(pin, value):
    print("in the play song part")
    audiofile = 'hozier.mp3'
    commandline = 'mplayer -af resample=48000:0:2 -slave -quiet -ao alsa:device=sysdefault=Set %s' % audiofile
    proc = subprocess.Popen(shlex.split(commandline), stdin=subprocess.PIPE)
    while (proc.poll() is None):
        if(stopState):
            print("made it to the breaky part")
            if (proc.poll() is None):
                
                proc.stdin.write('stop\n')
            break

@blynk.handle_event('write V1')
def stop(pin, value):
    print("changing stop state")
    stopState = True
    
    
if __name__ == '__main__':
    while True:
        blynk.run()  
    
    

	    
        