#!/usr/bin/env python3
# From: https://graycat.io/tutorials/beaglebone-io-using-python-mmap/
# Edited by Emily Dougherty
from mmap import mmap
import time, struct


GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
USR3 = 1<<17 #p9_23 

# Next we need to make the mmap, using the desired size and offset:
with open("/dev/mem", "r+b" ) as f:
  mem = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)

# grab the whole 4-byte register:
packed_reg = mem[GPIO_OE:GPIO_OE+4]

# it will return the 32 bits 
reg_status = struct.unpack("<L", packed_reg)[0]

# configure the LED as an output by clearing its bit:
reg_status &= ~(USR3)

# Now all that's left to do is to pack it little-endian back into a string and update the mmap:

mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)

#toggle the LED by setting and clearing the bit:
try:
  while(True):
    mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", USR3)

    mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", USR3)
 
except KeyboardInterrupt:
  mem.close()