import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
scoreboard=Scoreboard()
car_manager=CarManager()



screen.listen()
screen.onkey(player.go_up,"Up")
screen.onkey(player.go_down,"Down")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()


    if player.ycor() == 280:
        print("end")
        player.move()

        scoreboard.increase_score()
        car_manager.update()

    for car in car_manager.all_cars:
        if player.distance(car) <20:
            scoreboard.game_over()
            game_is_on=False





