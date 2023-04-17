from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_pos()

    def move(self):
        self.forward(20)

    def bounce_v(self):
        self.dir = 360 - self.dir
        self.setheading(self.dir)

    def bounce_h(self):
        self.dir = 180 - self.dir
        if self.dir < 0:
            self.dir += 360
        self.setheading(self.dir)

    def reset_pos(self):
        self.pos = (0, 0)
        self.goto(self.pos)
        self.dir = random.randint(0, 360)
        self.setheading(self.dir)
