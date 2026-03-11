#!/bin/bash
df -h | awk 'NR>1 {gsub("%","",$5); if ($5 > 70) print "WARNING:",$1,$5"%"} >> op.txt

