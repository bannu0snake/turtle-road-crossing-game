from turtle import Turtle
import random as rand

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_car(self):
        chance = rand.randint(0, 6)
        if chance == 1:

            new = Turtle('square')

            new.shapesize(1, 2)
            new.color(rand.choice(COLORS))
            new.penup()
            new.goto(300, rand.randint(-240, 240))
            self.all_cars.append(new)

    def move_forward(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increment(self):
        self.car_speed += MOVE_INCREMENT
        self.move_forward()


