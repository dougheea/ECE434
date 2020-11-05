#!/usr/bin/env python3
from pydub import AudioSegment
from pydub.playback import play
import threading
import ctypes
import time
import blynklib
import blynktimer
import sys
import os

sound = AudioSegment.from_mp3('hozier.mp3')

def playSound():
    try:
        play(sound)
    except KeyboardInterrupt:
        print("Stopping playing")
        
    
if __name__ == "__main__":
    x = threading.Thread(target=playSound())
    print("Main    : before running thread")
    x.start()
    print("Main    : wait for the thread to finish")
    # x.join()
    print("Main    : all done")