#!/usr/bin/env python3

# Python program raising 
# exceptions in a python 
# thread 

import threading
import ctypes
import time
import blynklib
import blynktimer
import sys
import os
from subprocess import Popen
from pydub import AudioSegment
from pydub.playback import play

# Get the authorization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
   
class thread_with_exception(threading.Thread): 
    def __init__(self, name): 
        threading.Thread.__init__(self) 
        self.name = name 
              
    def run(self): 
  
        # target function of the thread class 
        try: 
            print("playing song")
            #while True: 
               # os.system("mplayer -ao alsa:device=sysdefault=Set hozier.mp3")
            sound = AudioSegment.from_mp3('hozier.mp3')
            play(sound)
            #time.sleep(8)
                #proc.kill()
                #proc.kill()

            #     # print('running ' + self.name)
            #     print("Playing Mariah Carey's 'All I Want For Christmas is You'")

        finally: 
            print('ended') 
           
    def get_id(self): 
  
        # returns id of the respective thread 
        if hasattr(self, '_thread_id'): 
            return self._thread_id 
        for id, thread in threading._active.items(): 
            if thread is self: 
                return id
   
    def raise_exception(self): 
        thread_id = self.get_id()
        proc.kill()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
              ctypes.py_object(SystemExit)) 
        if res > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
            print('Exception raise failure') 
            
            
@blynk.handle_event('write V0')
def song1(pin, value):

    
    t1 = thread_with_exception('Thread 1')
    t1.start()
    time.sleep(10) 
    t1.raise_exception() 
    #ti.kill()
    print("getting id")
    #pid = ti.get_id()
    t1.join() 
    
    
while True: 
    blynk.run()
       
