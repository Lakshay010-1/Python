from turtle import Turtle
from info import WINDOW_HEIGHT, WINDOW_WIDTH


class ScoreBoard(Turtle):

    def __init__(self, wh=WINDOW_HEIGHT, ww=WINDOW_WIDTH):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.window_height = wh
        self.window_width = ww
        self.refresh_score()

    def increment_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def refresh_score(self):
        self.teleport(0, self.window_height / 2)
        self.clear()
        self.color("white")
        self.write(
            f"Score : {self.score}", align="center", font=("Arial", 18, "normal")
        )
