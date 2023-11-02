#!/bin/bash

number=1
while [[ $number -lt 50 ]]
do
    echo $number
    let number=number+2
done