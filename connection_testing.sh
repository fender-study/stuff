#!/bin/bash

output="$(ping -c 3 $1)"

if [[ "$output" == *"100% packet loss"* ]]
then
    echo "The connection to $1 is not working."
else
    echo "The connection to $1 is working."
    echo "$output"
fi