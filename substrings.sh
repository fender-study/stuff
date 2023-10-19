#!/bin/bash

str1="Nowadays, Linux powers the servers of the internet"

if [[ "$str1" == *"linux"* ]]
then
    echo "The string contains word Linux"
else
    echo "The string does not contain word Linux"
fi