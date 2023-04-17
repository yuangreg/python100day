from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0

    def show_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=("Arial", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=("Arial", 70, "normal"))

    def update_score(self, player):
        if player == "l":
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.show_score()
