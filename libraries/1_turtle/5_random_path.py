from random import choice, randint
from turtle import Turtle, Screen, colormode

t_obj = Turtle()
colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    random_colors = (r, g, b)
    return random_colors



t_obj.shape("turtle")
t_obj.pensize(10)
t_obj.speed(0.5)

direction =[0, 90, 180, 270]


def random_walk():
    change_angle = choice(direction)
    t_obj.right(change_angle)
    t_obj.forward(30)


for i in range(1000):
    t_obj.color(random_color())
    random_walk()


screen_obj = Screen()
screen_obj.screensize(500, 500)
screen_obj.exitonclick()
