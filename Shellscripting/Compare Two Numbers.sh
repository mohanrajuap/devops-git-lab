#!/bin/bash
echo "enter number1"
read N1
echo "enter number2"
read N2
if [ $N1 -gt 0 ] && [ $N2 -gt 0 ]
then
echo "both $N1 and $N2 is postive"
elif [ $N1 -gt 0 ]
then
echo "$N1 is postive"
elif [ $N2 -gt 0 ]
then
echo "$N2 is postive"
elif [ $N1 -le 0 ] && [ $N2 -le 0 ]
then
echo "both $N1 and $N2 is negative"
else
echo "good"
fi
