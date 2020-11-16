#!/usr/bin/python3
# ////////////////////////////////////////
# //	neopixelRainbow.py
# //	UDisplays a moving rainbow pattern on the NeoPixels
# //	Usage:	Run neopixelRpmsg.c on the PRU, Run neopixelRainbow.py on the ARM
# //	Wiring:	See neopixelRpmsg.c for wiring
# //	Setup:	Run neopixelRpmsg.c on the PRU
# //	See:	 
# //	PRU:	Runs on ARM
# ////////////////////////////////////////
from time import sleep
import math
import random

len = 240

def red_green_blink():
    global fo
    global len
    phase = 0
    
    for k in range(0, 10):
        if (phase%2) == 0:
            for i in range(0, len):
                if (i%2) == 0:
                    r = 100
                    g = 0x00
                    b = 0x00
                else:
                    r = 0x00
                    g = 100
                    b = 0x00
                
                fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
        else:
            for i in range(0, len):
                if (i%2) == 0:
                    r = 0x00
                    g = 100
                    b = 0x00
                else:
                    r = 100
                    g = 0x00
                    b = 0x00
                
                fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
    
        fo.write("-1 0 0 0\n".encode("utf-8"));
        phase = phase + 1
        sleep(0.5)

def red_run_forward():
    global fo
    global len
    
    for k in range(0, len):
        for i in range(0, len):
            if(i == k):
                r = 100
                g = 0x00
                b = 0x00
            else:
                r = 0x00
                g = 0x00
                b = 0x00
            
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
        
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.01)
        
def red_add_forward():
    global fo
    global len
    
    for k in range(0, len):
        for i in range(0, len):
            if(i <= k):
                r = 100
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
    
    for k in range(len, 0, -1):
        for i in range(0, len):
            if(i == k):
                r = 100
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
    
    for k in range(0, len):
        for i in range(0, len):
            if(i >= k):
                r = 100
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

    run_length = len     #determines how far down the string the red and green will run
    
    for k in range(0, run_length, 1):
        for i in range(0, len):
            if(i == k):
                r = 100
                g = 0x00
                b = 0x00
            elif(i == (run_length-k)):
                r = 0x00
                g = 100
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
                r = 100
                g = 0x00
                b = 0x00
            elif(i == (run_length-k)):
                r = 0x00
                g = 100
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
    
    for k in range(0, 100):
        for i in range(0, len):
            fo.write("%d %d %d %d\n".encode("utf-8") % (i, k, g, b))
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.005)
    
    for k in range(100, 0, -1):
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
            r = 100
            g = 0x00
            b = 0x00
        else:
            r = 0x00
            g = 100
            b = 0x00
        
        fo.write("%d %d %d %d\n".encode("utf-8") % (ledNum, r, g, b))
        fo.write("-1 0 0 0\n".encode("utf-8"));
        sleep(0.1)


def off():
    global fo
    global len
    
    for k in range(0, len):
        fo.write("%d %d %d %d\n".encode("utf-8") % (k, 0, 0, 0))

    fo.write("-1 0 0 0\n".encode("utf-8"));
    sleep(0.1)


def half_n_half():
    global fo 
    global len

    for k in range (0, len):
        if k > (len/2):
            r = 100
            g = 0x00
            b = 0x00
        else:
            r = 0x00
            g = 100
            b = 0x00

        fo.write("%d %d %d %d\n".encode("utf-8") % (k, r, g, b))

    fo.write("-1 0 0 0\n".encode("utf-8"))
    

        

# Main is below

# Open a file
fo = open("/dev/rpmsg_pru30", "wb", 0)  # Write binary unbuffered

# red_green_blink()
while(True):
     #red_run_backward()
    # red_run_forward()
    # red_green_run()
    pulse_red()
    # pulse_wave()
    # randomLED()
    #red_add_forward()
    #red_add_backward()
    #half_n_half()
    # off()
    
# Close opened file
fo.close()