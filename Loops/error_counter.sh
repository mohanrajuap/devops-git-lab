#!/bin/bash
c=$(grep 'error' /mnt/d/Devops_practice/loops/app.log | wc -l)
if [ $c -ge 0 ]
then
echo "error found in log and count is $c"
else
echo "no error found in log"
fi