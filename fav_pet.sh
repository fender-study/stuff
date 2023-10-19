#!/bin/bash

echo -n "Enter your favorite pet: "
read PET

case "$PET" in
    dog)
        echo "Your favorite pet is dog."
        ;;
    cat|Cat)
        echo "You like cats."
        ;;
    fish|"Arfican Turtle")
        echo "Fish and turtles are great."
        ;;
    *)
        echo "Your fav pet in unknown."
esac