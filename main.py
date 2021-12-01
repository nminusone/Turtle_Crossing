import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
score = Scoreboard()
sam = Player()
a_car = CarManager()
level_1 = 10
list_of_cars = []
screen.onkey(fun=sam.move, key='Up')

# making_cars = True
# while making_cars:
#     for _ in range(level_1):
#         cars = CarManager()
#         list_of_cars.append(cars)
#     making_cars = False
counter = 0
game_is_on = True
while game_is_on:
    time.sleep(a_car.screen_speed)
    screen.update()
    if counter % 6 == 0:
        cars = CarManager()
        list_of_cars.append(cars)
    for car in list_of_cars:
        car.move()
        if sam.distance(car) < 15:
            score.turtle_died()
            game_is_on = False
        if sam.ycor() > sam.finish:
            score.turtle_made_it()
            sam.restart()
            a_car.speed_up()
            print(a_car.screen_speed)

    counter += 1
screen.exitonclick()
