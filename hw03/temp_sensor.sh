#!/bin/bash
temp=`i2cget -y 2 0x48` #retrieve data from temp sensor 1
temp2=`i2cget -y 2 0x49` #retrieve data from temp sensor 2

tempcut="${temp:2:4}" #take the 2 least signifigant digits (omits the 0x)
tempcut2="${temp2:2:4}"

tempdec=$((16#$tempcut)) #convert to decimal
tempdec2=$((16#$tempcut2))

tempmul=$(($tempdec*9/5)) #converting to F
tempmul2=$(($tempdec2*9/5))

tempf=$(($tempmul+32))
tempf2=$(($tempmul2+32))

echo "${tempf}" #output degrees in F
echo "${tempf2}"