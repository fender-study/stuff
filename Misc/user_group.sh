#!/bin/bash

read -p "Please enter a group name" group
read -p "Please enter a username" username

groupadd $group
useradd -s /bin/bash -m -G $group $username

tail -n 2 /etc/group
echo
tail -n 2 /etc/passwd
echo

echo "The group $group and user $username were created."
