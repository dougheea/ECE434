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

len = 40
amp = 12
f = 44
shift = 3
phase = 0

# Open a file
fo = open("/dev/rpmsg_pru30", "wb", 0)  # Write binary unbuffered

for i in range(0, len):
    # r = (amp * (math.sin(2*math.pi*f*(i-phase-0*shift)/len) + 1)) + 1;
    # g = (amp * (math.sin(2*math.pi*f*(i-phase-1*shift)/len) + 1)) + 1;
    # b = (amp * (math.sin(2*math.pi*f*(i-phase-2*shift)/len) + 1)) + 1;

    r = 0
    g = 0
    b = 0
    
    fo.write("%d %d %d %d\n".encode("utf-8") % (i, r, g, b))
    # print("0 0 127 %d" % (i))

fo.write("-1 0 0 0\n".encode("utf-8"));

# Close opened file
fo.close()