#!/bin/bash
echo "Please enter the log file name"
read logname
if [ -f $logname ]
then
echo "checking errors"
c=$(grep -i 'error' $logname)
echo "Errors found $c"
else
echo "no errors"
fi


###############################################################
#!/bin/bash

echo "Please enter the log file name"
read logname

if [ -f "$logname" ]
then
    echo "Checking errors..."
    c=$(grep -ic "error" "$logname")

    if [ $c -gt 0 ]
    then
        echo "Errors found: $c"
    else
        echo "No errors found"
    fi
else
    echo "File does not exist"
fi