#!/bin/bash

read -p "Enter positive integer: " number

if [[ $number -gt 0 && $number -lt 100 ]]
    then
        i=0
        while [[ i -lt $number ]]
        do
            sleep 3
            name=$(date +%M:%S)
            touch $name.txt
            let i=i+1
        done
        echo "$number text files where created."
    else
        echo "Wrong integer. Exiting."
        sleep 1
        exit
fi