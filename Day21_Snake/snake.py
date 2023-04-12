import turtle

START_POS = [(0, 0), (0, 0), (0, 0)]
MOVE_DISTANCE = 20
UP, DOWN, RIGHT, LEFT = 90, 270, 0, 180


class Snake:
    def __init__(self):
        self.body = []
        self.init_body()
        self.head = self.body[0]

    def init_body(self):
        for pos in START_POS:
            segment = self.extend(pos)
            self.body.append(segment)

    def grow(self):
        pos = self.body[-1].position()
        self.extend(pos)

    def extend(self, pos):
        segment = turtle.Turtle("square")
        segment.color('white')
        segment.penup()
        segment.goto(pos)
        self.body.append(segment)
        return segment

    def move(self):
        for ind in range(len(self.body)-1, 0, -1):
            new_segment = self.body[ind-1]
            new_x = new_segment.xcor()
            new_y = new_segment.ycor()
            self.body[ind].goto((new_x, new_y))
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
