#!/bin/bash
echo "1.copying file"
echo "2.moving file"
echo "3.check memory available"

read value

case $value in
1)
echo "copying"
;;
2)
echo "moving"
;;
3)
echo "memory checK"
;;
esac
