#!/bin/bash
LOG_DIR="/mnt/d/Devops_practice/L2scripts"
LOG_FILE="$LOG_DIR/app.log"

if [ -f "$LOG_FILE" ]; then
    mv "$LOG_FILE" "$LOG_DIR/app.log-$(date +%Y-%m-%d_%H-%M-%S)"
    touch "$LOG_FILE"
    echo "Log rotated successfully."
else
    echo "No log file found at $LOG_FILE"
fi