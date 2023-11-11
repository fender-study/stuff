#!/bin/bash

while true
do
    output="$(pgrep -l $1)"
    if [[ -n "$output" ]]
    then
        echo "The process \"$1\" is running."
    else
        echo "The process \"$1\" is NOT running."
    fi
    sleep 3
done