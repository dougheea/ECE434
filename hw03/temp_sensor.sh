#!/bin/bash
temp=`i2cget -y 2 0x48`
temp2=`i2cget -y 2 0x49`

tempcut="${temp:2:4}"
tempcut2="${temp2:2:4}"

tempdec=$((16#$tempcut))
tempdec2=$((16#$tempcut2))

tempmul=$(($tempdec*9/5))
tempmul2=$(($tempdec2*9/5))

tempf=$(($tempmul+32))
tempf2=$(($tempmul2+32))

echo "${tempf}"
echo "${tempf2}"