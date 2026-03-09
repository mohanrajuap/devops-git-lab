#!/bin/bash
adding()
{
    sum=$(($1 + $2))
    echo "sum is $sum"
}

adding "$1"  "$2"
