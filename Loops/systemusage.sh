#!/bin/bash
echo "number of times checks needs to be perfomred"
read num
i=1
threshold_limit=80
while [ $i -le $num ]
do
echo "do the check the $i"
usage=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
if [ $usage -gt $threshold_limit ]
then
echo "CPU usage is above $threshold_limit"
else
echo "CPU usage is normal $usage"
fi
sleep 2
i=$(( i+1 ))
done