from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        """Player movement"""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_on_finish(self):
        """Returns True if player on the finish line"""
        if self.ycor() == FINISH_LINE_Y:
            return True

    def refresh(self):
        """Restarts position of a player"""
        self.goto(STARTING_POSITION)
