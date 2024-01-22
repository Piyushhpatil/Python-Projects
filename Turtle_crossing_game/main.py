import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

score = Scoreboard()

car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()

    for cars1 in car.cars:
        if cars1.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.finish_line():
        player.start()
        car.increase()
        score.increment()



screen.exitonclick()
