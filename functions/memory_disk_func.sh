#!/bin/bash
diskusgae()
{
    df -h
}

Memoryusage()
{
    free -m
}

echo "calling functions"

diskusgae
Memoryusage