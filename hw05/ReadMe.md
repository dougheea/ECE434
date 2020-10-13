# hw05 grading

| Points      | Description |
| ----------- | ----------- |
|  2 | Project - *LED wreath - Nice idea*
|  2 | Makefile
|  4 | Kernel Source
|  2 | Cross-Compiling
|  8 | Kernel Modules: hello, ebbchar, gpio_test, led
|  2 | Extras
| 20 | **Total**

*My comments are in italics. --may*

### Makefile
The makefile is used to compile the app.c script. Makefile can be run from the command line by typing 'make'. The script will compile the script, build the executable, and print a successful message if everything went smoothly. The executable that can then be run is 'app.arm'. You can also see the compiler used by typing 'make test'.

### gpio_test Folder
This folder contains the .c and makefile for running the kernel module gpio test. This is kernel module that uses 2 buttons to turn on 2 corresponding LEDS. I use GPIO pins 50 & 14 for the LEDS and pins 49 & 117 for the buttons. To run the program, first run the make file. Then insert the module by typing "sudo insmod gpio test.ko". The program should be running. Finally exit by typing sudo rmmod gpio_test". 

### led Folder
This folder contains led.c and a makefile. The overall goal of these files is to make 2 LEDS blink at different periods. The LEDs are on pin p9-14 and p9-26. First the make file must be run. Then insert the module by typing "sudo insmod led.ko". The program should be running. Finally exit by typing sudo rmmod led". You can check the messages that the program printed out by typing "dmesg -H | tail -4".

### hw05images pdf
This pdf contains all the images collected from completing other parts of the homework. These images include completing: swapping kernels, cross compiling and completing the different kernel modules.

*Nice documentation*