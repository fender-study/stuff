#!/bin/bash

PS3="Your choice: "

select ITEM in "Add User" "List all processes" "Kill process" "Install program" "Quit"

do
    if [[ $REPLY -eq 1 ]]
    then
        read -p "Enter the username: " username
        output="$(grep -w $username /etc/passwd)"
        if [[ -n "output" ]]
        then
            echo "User with such name already exists."
        else
            sudo useradd -m -s /bin/bash "$username"
            if [[ $? -eq 0 ]]
            then
                echo "The user $username createrd successfully."
                tail -n 1 /etc/passwd
            else
                echo "There was an error adding a user $username."
            fi
        fi
    elif [[ $REPLY -eq 2 ]]
    then
        echo "Listing all processes..."
        sleep 1
        ps -ef
    elif [[ $REPLY -eq 3 ]]
    then
        read -p "Enter the process to kill: " process
        pkill $process
    elif [[ $REPLY -eq 4 ]]
    then
        read -p "Enter the program to install: " app
        sudo apt update && sudp apt install $app
    elif [[ $REPLY -eq 5 ]]
    then
        echo "Quitting..."
        sleep 1
        exit
    else
        echo "Invalid menu selection."
    fi
done