import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player((0, -280))
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(key='Up', fun=player.move_up)

game_on = True
while game_on:
    car.create_car()
    car.move_forward()
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 270:
        score.update_score()
        car.increment()
        player.reset()
    for c in car.all_cars:
        if c.distance(player) < 20:
            score.colloid()
            game_on = False

screen.exitonclick()
