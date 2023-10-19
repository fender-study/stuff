#!/bin/bash

function print_statement () {
    echo "This printed from function"
}

display_something () {
    echo "Hello from function"
}

print_statement
display_something

function create_files () {
    echo "Creating $1"
    touch $1
    chmod 400 $1
    sleep 2
    echo "Creating $2"
    touch $2
    chmod 600 $2
}

create_files a.txt b.txt