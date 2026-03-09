#!/bin/bash

echo "1. COPY FILE"
echo "2. MOVE FILE"
echo "3. DELETE FILE"

read value

case $value in

1)
   echo "Enter source file:"
   read src
   echo "Enter destination:"
   read dest
   cp "$src" "$dest"
   ;;

2)
   echo "Enter source file:"
   read src
   echo "Enter destination:"
   read dest
   mv "$src" "$dest"
   ;;

3)
   echo "Enter file to delete:"
   read file
   rm "$file"
   ;;

*)
   echo "Invalid option"
   ;;

esac