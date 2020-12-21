from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor('black')


tim = Turtle()
tim.color('cyan')
tim.speed('fastest')


def star():
    for _ in range (5):
        tim.forward(150)
        tim.left(144)





num = 90
while num != 0:

    star()
    new_pointing = tim.heading() + 5
    tim.setheading(new_pointing)
    num -= 1



screen.exitonclick()
