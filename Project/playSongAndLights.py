#!/usr/bin/env python3
#Authors: Emily Dougherty and Ryan Taylor
#This program uses a Blynk app to control a string of nano LEDs and play a christmas song
#once thir corresponding button is pressed. The song/lights will stop if the Blynk 'stop button'
#is pressed. The setup.sh files must be sourced before running this program.

import blynklib
import blynktimer
import sys
import os
import logging
import threading
import time
from time import sleep
import ctypes
import subprocess
import math
import random

# Get the authorization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH')

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
global off
global song
global threadCheck
threadCheck = False
off = 0

global maxBrightness
maxBrightness = 100

fo = open("/dev/rpmsg_pru30", "wb", 0)  # Write binary unbuffered

@blynk.handle_event('write V0')
def song1(pin, value):
    global song
    global threadCheck
    if(threadCheck == False):
        print("starting All I Want For Christmas")
        threadCheck = True
        song = "AllIWantForChristmas.mp3"
        songThread = threading.Thread(target = helperFunction1)
        songThread.start()
    else:
        print("already playing a song!")

@blynk.handle_event('write V2')
def song2(pin, value):
    global song
    global threadCheck
    if(threadCheck == False):
        print("starting Merry Christmas, Happy Holidays")
        threadCheck = True
        song = "NSYNC.mp3"
        songThread = threading.Thread(target = helperFunction2)
        songThread.start()
    else:
        print("already playing a song!")
    
@blynk.handle_event('write V3')
def song3(pin, value):
    global song
    global threadCheck
    if(threadCheck==False):
        print("starting Sleigh Ride")
        threadCheck = True
        song = "SleighRide.mp3"
        songThread = threading.Thread(target = helperFunction3)
        songThread.start()
    else:
        print("already playing a song!")
    
@blynk.handle_event('write V4')
def song4(pin, value):
    global song
    global threadCheck
    if(threadCheck==False):
        print("starting Carol of the Bells")
        threadCheck = True
        song = "CarolOfTheBells.mp3"
        songThread = threading.Thread(target = helperFunction4)
        songThread.start()
    else:
        print("already playing a song!")
    
@blynk.handle_event('write V1')
def stop(pin, value):
    global off
    off = 1
    
#All I want for christmas
def helperFunction1():
    global off
    global song
    global threadCheck
    player = subprocess.Popen(["mplayer", "-quiet", song], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(4)
    while(off == 0):
        red_green_blink()
        if(off == 1):
            break
        red_green_blink()
        if(off == 1):
            break
        red_run_forward()
        if(off == 1):
            break
        red_run_backward()
        if(off == 1):
            break
        pulse_wave()
        if(off == 1):
            break
        randomLED()
    player.communicate(b"q")
    off = 0
    Lightsoff()
    threadCheck = False
    
  
 #NSYNC   
def helperFunction2():
    global off
    global song
    global threadCheck
    player = subprocess.Popen(["mplayer", "-quiet", song], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(4)
    while(off == 0):
        half_n_half()
        if(off == 1):
            break
        sleep(3)
        pulse_red()
        if(off == 1):
            break
        pulse_wave()
        if(off == 1):
            break
        red_green_blink()
        if(off == 1):
            break
        red_green_run() 
        if(off == 1):
            break
    player.communicate(b"q")
    off = 0
    Lightsoff()
    threadCheck = False
   
 #Sliegh ride   
def helperFunction3():
    global off
    global song
    global threadCheck
    player = subprocess.Popen(["mplayer", "-quiet", song], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(4)
    while(off == 0):
        red_green_blink()
        if(off == 1):
            break
        red_run_backward()
        if(off == 1):
            break
        pulse_wave()
        if(off == 1):
            break
        randomLED()
    player.communicate(b"q")
    off = 0
    Lightsoff()
    threadCheck = False

    
#Carol of the bells    
def helperFunction4():
    global off
    global song
    global threadCheck
    player = subprocess.Popen(["mplayer", "-quiet", song], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(4)
    while(off == 0):
        red_green_blink()
        if(off == 1):
            break
        red_green_blink()
        if(off == 1):
            break
        red_run_forward()
        if(off == 1):
            break
        red_run_backward()
        if(off == 1):
            break
        randomLED()
        
    player.communicate(b"q")
    off = 0
    Lightsoff()
    threadCheck = False
    
#The Light Animations:
#red_green_blink()
#red_run_forward()
#red_run_backward()
#red_green_run()    
#pulse_red()
#pulse_wave()
#randomLED()
#half_n_half():
#red_add_forward()
#red_add_backward()


len = 240

def red_add_forward():
    global fo
    global len
    global maxBrightness
    
    for k in range(0, len):
        for i in range(0, len):
            if(i <= k):
                r = maxBrightness
                g = 0x00
                b = 0x00
            else:
                r = 0x00
                g = 0x00
                b = 0x00
            
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
        
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.01)
        
def red_add_backward():
    global fo
    global len
    global maxBrightness
    
    for k in range(0, len):
        for i in range(0, len):
            if(i >= k):
                r = maxBrightness
                g = 0x00
                b = 0x00
            else:
                r = 0x00
                g = 0x00
                b = 0x00
            
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
        
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.01)

def red_green_blink():
    global fo
    global len
    global maxBrightness
    phase = 0
    
    for k in range(0, 10):
        if (phase%2) == 0:
            for i in range(0, len):
                if (i%2) == 0:
                    r = maxBrightness
                    g = 0x00
                    b = 0x00
                else:
                    r = 0x00
                    g = maxBrightness
                    b = 0x00
                
                fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
        else:
            for i in range(0, len):
                if (i%2) == 0:
                    r = 0x00
                    g = maxBrightness
                    b = 0x00
                else:
                    r = maxBrightness
                    g = 0x00
                    b = 0x00
                
                fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
    
        fo.write("-1 0 0 0\n".encode("utf-8"));
        phase = phase + 1
        sleep(0.5)

def red_run_forward():
    global fo
    global len
    global maxBrightness
    
    for k in range(0, len):
        for i in range(0, len):
            if(i == k):
                r = maxBrightness
                g = 0x00
                b = 0x00
            else:
                r = 0x00
                g = 0x00
                b = 0x00
            
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
        
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.01)
    
def red_run_backward():
    global fo
    global len
    global maxBrightness
    
    for k in range(len, 0, -1):
        for i in range(0, len):
            if(i == k):
                r = maxBrightness
                g = 0x00
                b = 0x00
            else:
                r = 0x00
                g = 0x00
                b = 0x00
            
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
        
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.01)
    
    
def red_green_run():
    global fo
    global len
    global maxBrightness

    run_length = len     #determines how far down the string the red and green will run
    
    for k in range(0, run_length, 1):
        for i in range(0, len):
            if(i == k):
                r = maxBrightness
                g = 0x00
                b = 0x00
            elif(i == (run_length-k)):
                r = 0x00
                g = maxBrightness
                b = 0x00
            else:
                r = 0x00
                g = 0x00
                b = 0x00
            
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
        
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.01)
        
    for k in range(run_length, 0, -1):
        for i in range(0, len):
            if(i == k):
                r = maxBrightness
                g = 0x00
                b = 0x00
            elif(i == (run_length-k)):
                r = 0x00
                g = maxBrightness
                b = 0x00
            else:
                r = 0x00
                g = 0x00
                b = 0x00
            
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
        
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.01)

def pulse_red():
    global fo 
    global len
    global maxBrightness
    
    g = 0x00
    b = 0x00
    
    for k in range(0, maxBrightness):
        for i in range(0, len):
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, k, g, b))
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.005)
    
    for k in range(maxBrightness, 0, -1):
        for i in range(0, len):
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, k, g, b))
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.005)


def pulse_wave():
    global fo 
    global len
    global maxBrightness
    
    amp = 12
    f = 44
    shift = 3
    phase = 0
    for k in range(0, 42):
        for i in range(0, len):
            r = (amp * (math.sin(2*math.pi*f*(i-phase-0*shift)/len) + 1)) + 1;
            g = (amp * (math.sin(2*math.pi*f*(i-phase-1*shift)/len) + 1)) + 1;
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, 0))
    
        fo.write("-1 0 0 0\n".encode("utf-8"));
        phase = phase + 1
        sleep(0.05)


def randomLED():
    global fo
    global len
    global maxBrightness
    
    for k in range(0, len):
        ledNum = random.randrange(len)
        if(ledNum%2 == 0):
            r = maxBrightness
            g = 0x00
            b = 0x00
        else:
            r = 0x00
            g = maxBrightness
            b = 0x00
        
        fo.write("%d %d %d %d\n".encode("utf-8") % (ledNum, r, g, b))
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.1)

def half_n_half():
    global fo 
    global len
    global maxBrightness

    for k in range (0, len):
        if k > (len/2):
            r = maxBrightness
            g = 0x00
            b = 0x00
        else:
            r = 0x00
            g = maxBrightness
            b = 0x00

        fo.write("%d %d %d %d\n".encode("utf-8") % (k, r, g, b))

    fo.write("-1 0 0 0\n".encode("utf-8"))

def Lightsoff():
    global fo
    global len
    global maxBrightness

    
    for k in range(0, len):
        fo.write("%d %d %d %d\n".encode("utf-8") % (k, 0, 0, 0))

    fo.write("-1 0 0 0\n".encode("utf-8"));
    sleep(0.1)    
        

    
if __name__ == "__main__":

    while(1):
        blynk.run()

   