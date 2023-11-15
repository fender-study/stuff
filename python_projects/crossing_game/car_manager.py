from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    speed = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(250, random.randint(-250, 250))
        self.shape("square")
        self.shapesize(1, 2)

    def move(self):
        """Function to move cars"""
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.ycor())
