#!/bin/bash
echo "enter username"
read name   
if [ "$name" = "admin" ] || [ "$name" = "superadmin" ]
then
echo "username is correct $name"
else
echo "Please enter correct username"
fi
