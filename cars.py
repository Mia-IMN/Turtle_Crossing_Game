
from turtle import Turtle
import random


COLORS = ["#D6C0B3", "#AB886D", "#493628", "#E4E0E1", "#B7B7B7", "#705C53"]
INITIAL_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPOT = []

for _ in range(-220, 220, 40):
    SPOT.append(_)

class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 3)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.choice(SPOT))
            new_car.setheading(180)
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)

    def move_forward(self, distance, increment):
        for car in self.all_cars:
            if car.xcor() > -350:
                car.forward(INITIAL_MOVE_DISTANCE + increment)
                if car.distance(distance) < 20:
                    return True

