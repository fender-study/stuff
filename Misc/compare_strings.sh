#!/bin/bash

read -p "Enter first string: " str1
read -p "Enter second string: " str2

if [[ "$str1" == "$str2" ]]
then
    echo "Strings are equal!"
else
    echo "Strings are different!"
fi

if [[ "$str1" != "$str2" ]]
then
    echo "The strings are not equal"
fi