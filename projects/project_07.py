# Turtle race

from turtle import Turtle, Screen
from random import randint, choice

all_turtles = []
no_turtles = 5
screen = Screen()
screen.setup(width=600, height=500)
y_pos = 200
y_distance = 400 / no_turtles
race_end_line = 250

screen.colormode(255)
user_guess = screen.textinput(
    title="Make you guess",
    prompt=f"Which turtle do you think will win 1-{no_turtles} starting top to bottom : ",
)
print(user_guess)


def random_color_val():
    return randint(0, 255)


for _ in range(no_turtles):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.speed("fastest")
    r = random_color_val()
    g = random_color_val()
    b = random_color_val()
    new_turtle.color((r, g, b))
    all_turtles.append(new_turtle)

for index, turtle in enumerate(all_turtles):
    turtle.penup()
    turtle.setpos(-250, y_pos)
    y_pos -= y_distance
    turtle.pendown()

race_on = True if user_guess else False

while race_on:
    # for index, turtle in enumerate(all_turtles):
    turtle_to_move = list(range(len(all_turtles)))
    for _ in range(len(all_turtles)):
        turtle_moving = choice(turtle_to_move)
        turtle = all_turtles[turtle_moving]
        if not race_on:
            break
        move = randint(1, 10)
        turtle.forward(move)
        race_on = race_on and (False if turtle.xcor() >= race_end_line else True)
        if not race_on:
            if turtle_moving+1 == user_guess:
                print(
                    f"Congratulations, Your guess was right. turtle at position {turtle_moving+1} won."
                )
            else:
                print(
                    f"Better luck next time, Your guess was wrong. turtle at position {user_guess} lost to position {turtle_moving+1} turtle."
                )
        turtle_to_move.remove(turtle_moving)

screen.exitonclick()
