from random import choice
from turtle import Turtle, Screen

t_obj = Turtle()
t_obj.shape("turtle")
t_obj.color("red")

colors =['yellow', 'firebrick', 'dark magenta']

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides

    for _ in range(number_of_sides):
        t_obj.forward(50)
        t_obj.right(angle)


for num in range(3, 100):
    clr = choice(colors)
    t_obj.color(clr)
    draw_shape(num)







screen_obj= Screen()

screen_obj.exitonclick()
