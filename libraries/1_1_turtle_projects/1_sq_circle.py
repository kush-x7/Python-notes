from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor('black')


tim = Turtle()
tim.color('cyan')
tim.speed('fast')


def square():
    for _ in range (4):
        tim.forward(200)
        tim.right(90)


num = 75
while num != 0:

    square()
    new_pointing = tim.heading() - 5
    tim.setheading(new_pointing)
    num -= 1



screen.exitonclick()
