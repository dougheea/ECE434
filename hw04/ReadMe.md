### etch_a_sketch_flask.py
This file allows the etch_a_sketch file to be controlled from a web browser pointed at 192.168.7.2:8081. For the LED matrix to work, the file i2cmatrix.py in the Matrix8x8 folder must be run.


### GPIOmmap.py
This files uses mmap to read the inputs of 2 buttons and turn on the corresponding LED by writing to their bit values.


### LEDtoggle.py
This file toggles GPIO pin P9_23 as fast as it can using mmap. The period was 11.160us, which is faster than the gpiod toggle using python, but not quite as fast as the C gpiod program. 


### tmpKernelDriver.sh
This shell script sets the tmp101 sensor at address 0x49 as a new device and uses the kernel driver to read the value of that device.