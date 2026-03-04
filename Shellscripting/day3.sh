#!/bin/bash
num=10
num1=20
echo "enter a value for num3"
read num3

if [ $num -le $num1 ]
then
echo "$num is less than $num1"
fi

echo "starting another task"
if [ $((num3 % 2)) -eq 0 ]
then
echo "$num3 is even number"
else
echo "$num3 is odd number"
fi

echo "checking number is postivie or not"
if [ $num3 -gt 0 ]
then
echo "its positive"
else
echo "its negative"
fi


echo "checking number details"
if [ $num -gt 0]
then
echo "$num is positive"
else
echo "$num is negative"
