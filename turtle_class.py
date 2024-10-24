# Turtle set up
from turtle import Turtle

class UserTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(x=0, y=-280)

    def move_forward(self):
        self.forward(10)
    #
    # def move_left(self):
    #     self.goto(self.xcor() - 20, self.ycor())
    #
    # def move_right(self):
    #     self.goto(self.xcor() + 20, self.ycor())
    #
    # def hit_car(self):
    #     if self.distance(1,1)