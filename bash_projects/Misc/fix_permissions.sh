#!/bin/bash

read -p "Enter a directory: " directory

echo "Changing direcories permission..."
find $directory -type d -exec chmod 755 {} \;
echo "Done."

echo "Changing file permissions..."
find $directory -type f -exec chmod 644 {} \;
echo "Done."