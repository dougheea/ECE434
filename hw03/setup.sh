#!/bin/bash
config-pin P8_11 eqep
config-pin P8_12 eqep
config-pin P8_33 eqep
config-pin P8_35 eqep

i2cset -y 2 0x48 0x02 0x14
i2cset -y 2 0x49 0x02 0x14


i2cset -y 2 0x48 0x03 0x16
i2cset -y 2 0x49 0x03 0x16