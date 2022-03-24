from turtle import  Turtle
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.move()



    def move(self):
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(0, -280)
        self.setheading(90)



    def go_up(self):
        self.forward(MOVE_DISTANCE)


    def go_down(self):
        self.back(MOVE_DISTANCE)

    # def end(self):
    #     if self.ycor() > FINISH_LINE_Y:
    #         scoreboard.increase_score()
