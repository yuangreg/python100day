from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor('black')
        self.screen.setup(width=800, height=600)
        self.screen.title("Pong")
        # Turn off animation during init
        self.screen.tracer(0)
        self.ball = Ball()
        self.score = Score()
        self.paddle1 = Paddle((-350, 0))
        self.paddle2 = Paddle((350, 0))
        self.init_play()

    def init_play(self):
        self.game_is_on = True
        self.screen.listen()
        self.screen.onkey(self.paddle1.go_up, "w")
        self.screen.onkey(self.paddle1.go_down, "s")
        self.screen.onkey(self.paddle2.go_up, "Up")
        self.screen.onkey(self.paddle2.go_down, "Down")
        self.score.show_score()

    def run_game(self):
        while (self.game_is_on):
            # when tracer(0), need to update the screen manually
            self.screen.update()
            self.ball.move()
            time.sleep(0.05)

            # Check bouncing condition
            x_cor, y_cor = self.ball.position()
            if y_cor > 290 or y_cor < -290:
                self.ball.bounce_v()

            # Check collision with paddle
            if self.ball.distance(self.paddle1)<50 and x_cor < -320:
                self.ball.bounce_h()
            if self.ball.distance(self.paddle2)<50 and x_cor > 320:
                self.ball.bounce_h()

            # Ball escape
            if self.ball.xcor() < -380:
                self.score.update_score('r')
                self.ball.reset_pos()
            if self.ball.xcor() > 380:
                self.score.update_score('l')
                self.ball.reset_pos()

        self.screen.exitonclick()

if __name__ == "__main__":
    game = Game()
    game.run_game()