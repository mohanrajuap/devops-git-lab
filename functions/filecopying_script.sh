#!/bin/bash
copyfunc()
{
    cp $1 $2
    echo "source path is $1"
    echo "destination path is $2"
}
copyfunc "$1" "$2"