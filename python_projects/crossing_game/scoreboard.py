from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-220, 240)
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_score(self):
        """Updates score screen every time player reaches finish line"""
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        """Declares end of the game if player lost"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
