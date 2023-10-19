#!/bin/bash

DIRECTORY="/home/fender/repository/python_study/Projects/Python/"

find "$DIRECTORY" -type d -name "venv" -exec rm -r {} \;