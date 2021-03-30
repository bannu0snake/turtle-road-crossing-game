from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(-200, 250)
        self.print_score()

    def print_score(self):
        self.write(f'score : {self.score}', font=FONT, align='center')

    def update_score(self):
        self.clear()
        self.score += 1
        self.print_score()

    def colloid(self):
        self.goto(0, 0)
        self.write('GAME OVER', font=FONT, align='center')
