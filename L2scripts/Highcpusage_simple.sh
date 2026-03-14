#!/bin/bash
c=$(top -b -n1 | awk '$8 > "80.0%" {print $1,$9}')
echo $c
