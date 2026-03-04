#!/bin/bash
echo "enter the filename"
read file
echo "enter the dirname"
read dir
if [ -f $file ] && [ -d $dir ]
then
echo "file and dir is present"
else
echo "file and dir is not present"
fi