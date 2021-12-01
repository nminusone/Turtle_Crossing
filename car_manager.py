import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 50


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(1, 2)
        self.penup()
        self.goto(280, random.randint(-225, 225))
        self.seth(180)
        self.count = 0
        self.screen_speed = 0.1
        self.speed = STARTING_MOVE_DISTANCE

    def speed_up(self):
        self.speed += MOVE_INCREMENT
        self.screen_speed *= 0.9

    def move(self):
        self.forward(self.speed)

    def car_count(self):
        self.count += 1
