from random import choice, randint
from turtle import Turtle, Screen, colormode

t_obj = Turtle()
colormode(255)
t_obj.speed(.5)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    random_colors = (r, g, b)
    return random_colors


def draw_circle(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        t_obj.color(random_color())
        t_obj.circle(100)
        t_obj.setheading(t_obj.heading() + size_of_gap)
        t_obj.circle(100)

draw_circle(5)

screen_obj = Screen()
screen_obj.screensize(500, 500)
screen_obj.exitonclick()
