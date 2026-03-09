#!/bin/bash
echo "enter option"
read option
case $option in
dev)
      echo "Deploying to Development"
      ;;
  test)
      echo "Deploying to Testing"
      ;;
  prod)
      echo "Deploying to Production"
      ;;
  *)
      echo "Invalid environment"
      ;;
esac