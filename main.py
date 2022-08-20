import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# define classes
player = Player()
score = Scoreboard()
cars = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.up, "Up")
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(1)
    screen.update()
    cars.create_cars()
    cars.move_car()

    #   detect collision with car
    for i in cars.all_cars:
        if i.distance(player) < 20:
            score.gameover()
            game_is_on = False

    # detect the other end of the screen
    if player.ycor() > 279:
        score.next_level()
        player.go_to_start()
        cars.increase_speed()

screen.exitonclick()
