#!/bin/bash
echo "Enter dir"
read dir
echo "Enter filename"
read fname
if [ -f $fname ] && [ -d $dir ]
then
echo "File and Dir present"
elif [ -f $fname ]
then
echo "only file is present"
elif [ -d $dir ]
then
echo "only dir is present"
else
echo "Both dir and file not present"
fi
