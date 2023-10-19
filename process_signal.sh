#!/bin/bash

if [[ $# -ne 2 ]]
then
    echo "Run the script with 2 arguments: Signal and PID"
    exit
fi

case "$1" in
    1)
        echo "Sending the SIGHUP to $2"
        kill -SIGHUP $2
        ;;
    2)
        echo "Sending the SIGINT to $2"
        kill -SIGINT $2
        ;;
    15)
        echo "Sending the SIGTERM to $2"
        kill -SIGTERM $2
        ;;
    9)
        echo "Sending the SIGKILL to $2"
        kill -SIGKILL $2
        ;;
    *)
        echo "Signal number $1 will not be delivered!"
        ;;
esac
