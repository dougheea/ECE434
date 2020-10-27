#### All Images referenced throughout this homework are in the images file!!!

### 2.6 Blinking an LED (through gpio)
To start the PRU examples I run this make command:  make TARGET=hello.pru0
To stop the PRU program I run this make command:  make TARGET=hello.pru0 stop

The fastest frequency I could get was 12.5MHz (as seen in table). The scope capture can be seen in the image called ARM_GPIOscope.

### 5.3 PWM Generator (pru)
There is an image of the scope output in this folder called PWMpruScope. The waveform is very stable and I did not see any jitter in it (once I made the wires connecting the probe much shorter).It ran at 50Mhz.

### 5.4 Controlling the PWM Frequency (Optional)
The ouput pins being driven by pwm4.pru0.c can be figured out by looking at the bit the R30 register is accessing of PRU0. In this program the output pins being driven are P9_31, P9_29, P9_30, and P9_28. The highest frequency I can get with 4 channel is: 326.8kHz. The image of the scope capture is called PWM4Channel.
When running the pwm-test.c program, I could see the output that said the count of each channel. When changing the count all I could do is change the parameters of the four loop to change the value of the count for each channel.


### 5.9 Reading an Input at Regular Intervals (Optional)

ADD TO READ ME USING THE SETUP FILE
By running input.pru0 I was able to use a button to turn on an LED using the pru. I used a scope to look at the difference between input and output. the difference was 97ns. The image image is called inputOutputScope.

### 5.10 Analog Wave Generator (optional)
I went through the exercise and took a picture of my scope capture for the sawtooth, sine, and triangle wave.


### Table of Results
|       |Frequency|Stability|
| ------------- | -------- |-------| 
|ARM GPIO  | 12.5MHz|Slightly unstable, wobbles every now and then|
|PRU GPIO |50MHz     |very stable|
|PWM Frequency| 326.8kHz| stable, didn't see any jitters)


