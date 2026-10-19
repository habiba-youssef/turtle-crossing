import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun= turtle.move, key="Up")

game_is_on = True
i = 0
car_list = []
move_increment = 10

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if i == 0 or i % 6 ==0:
        car = CarManager()
        car_list.append(car)

    for car in car_list:
        car.move(move_increment)

        # Detect if turtle collides with car
        if turtle.distance(car) <= 20:
            game_is_on = False

        # Detect if player wins , reaches finish line
        if turtle.level_up():
            scoreboard.level += 1
            scoreboard.update()
            move_increment += 2

    i +=1

scoreboard.game_over()
screen.exitonclick()