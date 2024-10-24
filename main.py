# set up the screen.
    # the screen should be 600 by 600
    # the screen should be white or milk
# create turtle
    # can move forward, left or right but not down
# create the car module
    # the cars should have different colors
    # the cars should be generated at random spot at regular intervals
# create a level module
    # should increase car speed when one level is passed
    # should take turtle back to the starting point
# The game is over when a car hits the turtle
    # should print GAME OVER on screen
import time
from turtle import Screen
from turtle_class import UserTurtle
from level import Level
from cars import Cars

# Screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#F5F5F7")
screen.title("Python Turtle Crossing Game")

# cars = Cars()
screen.tracer(0)
timmy = UserTurtle()
level = Level()

cars = Cars()

game_is_on = True
increment = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_forward(timmy.position(), increment)

    if cars.move_forward(timmy.position(), increment):
        screen.ontimer(level.game_over, 20)
        game_is_on = False

    if timmy.ycor() == 300:
        increment += 1
        screen.ontimer(level.level_up, 20)
        timmy.initial_position()

    level.current_level()


    screen.listen()
    screen.onkey(timmy.move_forward, "Up")
    # screen.onkey(timmy.move_left, "Left")
    # screen.onkey(timmy.move_right, "Right")


screen.exitonclick()
