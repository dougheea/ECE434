### Makefile
The makefile is used to compile the app.c script. Makefile can be run from the command line by typing 'make'. The script will compile the script, build the executable, and print a successful message if everything went smoothly. The executable that can then be run is 'app.arm'. You can also see the compiler used by typing 'make test'.

### gpio_test Folder
This folder contains the .c and makefile for running the kernel module gpio test. This is kernel module that uses 2 buttons to turn on 2 corresponding LEDS. I use GPIO pins 50 & 14 for the LEDS and pins 49 & 117 for the buttons. To run the program, first run the make file. Then insert the module by typing "sudo insmod gpio test.ko". The program should be running. Finally exit by typing sudo rmmod gpio_test". 