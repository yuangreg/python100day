from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)
        self.pos = pos

    def go_up(self):
        x, y = self.pos
        self.pos = x, y+10
        self.goto(self.pos)


    def go_down(self):
        x, y = self.pos
        self.pos = x, y - 10
        self.goto(self.pos)
