import turtle, time
from Day21_Snake.snake import Snake
import random

BOARD_WIDTH = 600
BOARD_HEIGHT = 600

class SnakeGame:

    def __init__(self):
        self.board = turtle.Screen()
        self.board.bgcolor("black")
        self.board.setup(width=BOARD_WIDTH, height=BOARD_HEIGHT)
        self.board.title("Snake Game")
        self.board.tracer(0)
        self.snake = Snake()
        self.score = -1
        self.init_score()
        self.game_is_on = True
        self.listen_input()
        self.init_food()

    def init_score(self):
        self.dumpturtle = turtle.Turtle("square")
        self.dumpturtle.color("white")
        self.dumpturtle.hideturtle()
        self.dumpturtle.penup()
        self.dumpturtle.goto(0, BOARD_HEIGHT/2-40)
        self.update_score()

    def game_end(self):
        self.dumpturtle.goto(0, 0)
        self.dumpturtle.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.dumpturtle.clear()
        self.dumpturtle.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def init_food(self):
        self.food = turtle.Turtle("square")
        self.food.color('red')
        self.refresh_food()

    def refresh_food(self):
        self.food.penup()
        x_cor = random.randint(-BOARD_WIDTH/2/20+1, BOARD_WIDTH/2/20-1) * 20
        y_cor = random.randint(-BOARD_WIDTH/2/20+1, BOARD_WIDTH/2/20-1) * 20
        self.food.goto((x_cor, y_cor))

    def collide_wall(self):
        x_cor, y_cor = self.snake.head.position()
        if x_cor > BOARD_WIDTH/2 - 10 or x_cor < - BOARD_WIDTH/2 + 10 or y_cor > BOARD_HEIGHT/2 - 10 or y_cor < - BOARD_HEIGHT/2 + 10:
            return True
        else:
            return False

    def collide_body(self):
        for seg in self.snake.body[3:]:
            if self.snake.head.distance(seg) < 10:
                return True
        return False

    def listen_input(self):
        self.board.listen()
        self.board.onkey(self.snake.move_up, "Up")
        self.board.onkey(self.snake.move_down, "Down")
        self.board.onkey(self.snake.move_left, "Left")
        self.board.onkey(self.snake.move_right, "Right")

    def start_game(self):
        while(self.game_is_on):
            self.board.update()
            time.sleep(0.05)
            self.snake.move()

            if self.snake.head.distance(self.food) < 10:
                self.refresh_food()
                self.snake.grow()
                self.update_score()

            if self.collide_wall() or self.collide_body():
                self.game_is_on = False
                self.game_end()

        self.board.exitonclick()

if __name__ == "__main__":
    my_game = SnakeGame()
    my_game.start_game()