#!/bin/bash
echo "1. Show disk usage"
echo "2. Show memory usage"
echo "3. Show system uptime"
echo "4. Exit"

read val

case $val in
1)
echo "displaying disk usage"
c=$(df -h)
echo $c
;;
2)
echo "displaying memory usage"
d=$(free -m)
echo $d
;;
3)
echo "displaying system uptime"
d=$(uptime)
echo $d
;;
4)
echo "exiting process"
exit 
esac