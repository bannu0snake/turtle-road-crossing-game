from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.left(90)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def reset(self):
        self.goto(STARTING_POSITION)
