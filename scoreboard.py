from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()

        self.goto(-250, 250)

        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f'Level:{self.level}', False, align='left', font=FONT)

    def turtle_made_it(self):
        self.level += 1
        self.update_level()

    def turtle_died(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', False, align='center', font=FONT)
