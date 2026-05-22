from turtle import Turtle
import random
from info import WINDOW_HEIGHT, WINDOW_WIDTH, GRID_SIZE


class Food(Turtle):

    def __init__(self, wh=WINDOW_HEIGHT, ww=WINDOW_WIDTH, padding=2):
        super().__init__()

        self.color("deep sky blue")
        self.shape("circle")
        self.speed("fastest")
        self.penup()

        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.window_width = ww - padding
        self.window_height = wh - padding

        self.refresh_pos()

    def refresh_pos(self):

        x = random.randrange(
            int(-self.window_width / 2 + GRID_SIZE),
            int(self.window_width / 2 - GRID_SIZE),
            GRID_SIZE,
        )

        y = random.randrange(
            int(-self.window_height / 2 + GRID_SIZE),
            int(self.window_height / 2 - GRID_SIZE),
            GRID_SIZE,
        )

        self.goto(x, y)
