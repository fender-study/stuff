import time
from turtle import Screen
from player import Player
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing road, THE GAME")

score = Scoreboard()

generation = 0

player = Player()
cars_list = []

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generating new car every 6 step
    if generation % 6 == 0:
        car = CarManager()
        cars_list.append(car)

    # Moving a car and checking for collision
    for wheel in cars_list:
        wheel.move()
        if player.distance(wheel) < 20:
            game_is_on = False
            score.game_over()

    # Checking if player reached finish line
    if player.is_on_finish():
        player.refresh()
        score.update_score()
        CarManager.speed += MOVE_INCREMENT
    generation += 1

screen.exitonclick()
