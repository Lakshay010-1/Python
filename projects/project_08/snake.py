from turtle import Turtle, Screen
import time
from food import Food
from scoreboard import ScoreBoard
from info import WINDOW_HEIGHT, WINDOW_PADDING, WINDOW_WIDTH, GRID_SIZE

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self, initial_size=3, wh=WINDOW_HEIGHT, ww=WINDOW_WIDTH, padding=2):

        # Score Board
        self.score_board = ScoreBoard()

        # Food
        self.food = Food()

        self.head_idx = 0
        self.snake = []

        self.window_height = wh
        self.window_width = ww

        self.boundaries = {
            "left": (-self.window_width / 2) + padding,
            "right": (self.window_width / 2) - padding,
            "up": (self.window_height / 2) - padding,
            "down": (-self.window_height / 2) + padding,
        }

        # Screen Initialization
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.listen()
        self.screen.onkeypress(self.turn_up, "Up")
        self.screen.onkeypress(self.turn_right, "Right")
        self.screen.onkeypress(self.turn_left, "Left")
        self.screen.onkeypress(self.turn_down, "Down")
        self.screen.tracer(0)
        self.screen.setup(
            width=self.window_width + WINDOW_PADDING,
            height=self.window_height + WINDOW_PADDING,
        )

        self.draw_boundary()

        # Initial Snake
        for i in range(initial_size):
            snake_part = self.construct_snake_part()
            if i == 0:
                self.snake_head = snake_part
            self.snake.append(snake_part)

        self.screen.update()

    def draw_boundary(self):
        worker = Turtle()
        worker.hideturtle()
        worker.color("white")
        worker.penup()
        worker.speed(10)
        worker.goto(self.boundaries.get("left"), self.boundaries.get("up"))
        worker.pendown()
        worker.goto(self.boundaries.get("right"), self.boundaries.get("up"))
        worker.goto(self.boundaries.get("right"), self.boundaries.get("down"))
        worker.goto(self.boundaries.get("left"), self.boundaries.get("down"))
        worker.goto(self.boundaries.get("left"), self.boundaries.get("up"))

    def construct_snake_part(self):
        snake_part = Turtle()
        snake_part.shape("square")
        snake_part.color("white")
        snake_part.penup()

        if len(self.snake) == 0:
            snake_part.goto(0, 0)
        else:
            snake_tail = self.snake[-1]
            x, y = snake_tail.pos()
            heading = snake_tail.heading()

            if heading == RIGHT:
                x -= GRID_SIZE

            elif heading == LEFT:
                x += GRID_SIZE

            elif heading == UP:
                y -= GRID_SIZE

            elif heading == DOWN:
                y += GRID_SIZE

            snake_part.goto(x, y)
        return snake_part

    def turn_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def turn_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def turn_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def turn_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def update_pos(self):
        for idx in range(len(self.snake) - 1, 0, -1):
            new_x, new_y = self.snake[idx - 1].pos()
            self.snake[idx].goto(new_x, new_y)

    def detect_food_collisions(self):
        if self.snake_head.distance(self.food) <= 10:
            self.snake.append(self.construct_snake_part())
            self.food.refresh_pos()
            self.score_board.increment_score()
            self.score_board.refresh_score()

    def head_body_collisions(self):
        for snake_part in self.snake[1:]:
            if self.snake_head.distance(snake_part) <= 15:
                return True
        return False

    def start(self):
        game_on = True
        while game_on:

            self.screen.update()
            time.sleep(0.05)

            self.update_pos()
            self.snake_head.forward(GRID_SIZE)

            self.detect_food_collisions()

            x_head, y_head = self.snake_head.pos()
            if (
                not (
                    self.boundaries["left"] < x_head < self.boundaries["right"]
                    and self.boundaries["down"] < y_head < self.boundaries["up"]
                )
                or self.head_body_collisions()
            ):
                game_on = False
                self.score_board.game_over()

        self.screen.exitonclick()
