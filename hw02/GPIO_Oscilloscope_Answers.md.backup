**Measuring a GPIO pin on an Oscilloscope Answers:**

### togglegpio.sh
1. min: 18.13mV
   max: 3.331V
2. 245ms period (This is when I kept ran it with a 0.1 sleep)
3. it is 145 ms away from 100ms
4. We are pinging gpio through bash, which is not known for speed
5. 22.5%
6. Here is the table with the period and processor values:

|Language       |Period(ms)|%Processor | Sleep Time (s)
|bash           |245       |22.5%      |0.1
|bash           |66.0      |72.8%      |0.01
|sh             |43.5      |79.2%      |0.01
|sh             |51.6      |66.5%      |0.005
|Python         |204       |3.3%       |0.1
|Python         |21.2      |3.7%       |0.01
|Python         |11.4      |15.8%      |0.005
|C              |
|gpiod py 1 bit |19 us    |100%
|gpiod py 2 bit |19.5 us  |100%
|gpiod c  1 bit |


7. it is pretty stable
8. Anytime I run vi the period is very noticeably less stable
9. There is minimal impact to the period
10. the period was 15ms shorter (see table)
11. 43.5ms (sleep time of 0.005 and using sh)

### Python
1. min: 40.31mV
   max: 3.327V
2. 21.00 ms
3. A lot smaller!
4. python is very fast
5. 3.7%
6. (see table above for full comparison)
7. Overall, it is pretty stable
8. Surprisingly the period is still rather stable when I use vi
9. shortest period I could get: 11.4ms

### C
1. min:
   max:
2. 


### gpiod
The fastest results for both the C and python files are added to the table above.