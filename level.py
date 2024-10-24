from turtle import Turtle

class Level(Turtle):

    def __init__(self,):
        super().__init__()
        self.game_level = 0
        self.hideturtle()
        self.penup()
        self.current_level()

    def current_level(self):
        self.clear()
        self.goto(x=-280, y=260)
        self.write(f"Level: {self.game_level}", align="left", font=("Courier", 18, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!!", align="center", font=("Courier", 18, "normal"))

    def level_up(self):
        self.goto(0, 0)
        self.game_level += 1
        self.write(f"Level Up!!", align="center", font=("Courier", 18, "normal"))
