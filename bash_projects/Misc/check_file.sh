#!/bin/bash

if [[ $# -eq 1 ]]
then
    if [[ -f "$1" ]]
    then
        echo "The argument is a file."
        sleep 1
        echo "Removing it's content..."
        echo "" > $1
    else
        echo "The argument is not a file."
    fi
else
    echo "The script requires only one argument."
fi