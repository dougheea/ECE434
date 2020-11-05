#!/usr/bin/env python3
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
off = 0

fo = open("/dev/rpmsg_pru30", "wb", 0)  # Write binary unbuffered

@blynk.handle_event('write V0')
def song1(pin, value):
    songThread = threading.Thread(target = helperFunction)
    songThread.start()
    print("after thread started")


@blynk.handle_event('write V1')
def stop(pin, value):
    global off
    print("in the STOP")
    off = 1

    
def helperFunction():
    global off
    player = subprocess.Popen(["mplayer", "-quiet", "AllIWantForChristmas.mp3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(off)
    time.sleep(4)
    while(off == 0):
        red_green_blink()
        red_run_backward()
        pulse_wave()
        randomLED()
    player.communicate(b"q")
    off = 0
    Lightsoff()
    print("everything DONE")
    

#The Light Animations:
#red_green_blink()
#red_run_forward()
#red_run_backward():
#red_green_run()    
#pulse_red()
#pulse_wave()
#randomLED()


len = 40

def red_green_blink():
    global fo
    global len
    phase = 0
    
    for k in range(0, 10):
        if (phase%2) == 0:
            for i in range(0, len):
                if (i%2) == 0:
                    r = 0xf0
                    g = 0x00
                    b = 0x00
                else:
                    r = 0x00
                    g = 0xf0
                    b = 0x00
                
                fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
        else:
            for i in range(0, len):
                if (i%2) == 0:
                    r = 0x00
                    g = 0xf0
                    b = 0x00
                else:
                    r = 0xf0
                    g = 0x00
                    b = 0x00
                
                fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
    
        fo.write("-1 0 0 0\n".encode("utf-8"));
        phase = phase + 1
        sleep(0.5)

def red_run_forward():
    global fo
    global len
    
    for k in range(0, 20):
        for i in range(0, len):
            if(i == k):
                r = 0xf0
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
    
    for k in range(20, 0, -1):
        for i in range(0, len):
            if(i == k):
                r = 0xf0
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

    run_length = 40     #determines how far down the string the red and green will run
    
    for k in range(0, run_length, 1):
        for i in range(0, len):
            if(i == k):
                r = 0xf0
                g = 0x00
                b = 0x00
            elif(i == (run_length-k)):
                r = 0x00
                g = 0xf0
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
                r = 0xf0
                g = 0x00
                b = 0x00
            elif(i == (run_length-k)):
                r = 0x00
                g = 0xf0
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
    
    g = 0x00
    b = 0x00
    
    for k in range(0, 200):
        for i in range(0, len):
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, k, g, b))
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.005)
    
    for k in range(200, 0, -1):
        for i in range(0, len):
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, k, g, b))
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.005)


def pulse_wave():
    global fo 
    global len
    
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
    
    for k in range(0, len):
        ledNum = random.randrange(len)
        if(ledNum%2 == 0):
            r = 0xf0
            g = 0x00
            b = 0x00
        else:
            r = 0x00
            g = 0xf0
            b = 0x00
        
        fo.write("%d %d %d %d\n".encode("utf-8") % (ledNum, r, g, b))
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.1)


def Lightsoff():
    global fo
    global len
    
    for k in range(0, len):
        fo.write("%d %d %d %d\n".encode("utf-8") % (k, 0, 0, 0))

    fo.write("-1 0 0 0\n".encode("utf-8"));
    sleep(0.1)    
        

    
if __name__ == "__main__":

    while(1):
        blynk.run()

   