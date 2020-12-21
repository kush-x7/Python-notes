from turtle import Turtle, Screen


screen = Screen()
screen.bgcolor('black')


tim = Turtle()
tim.color('cyan')
tim.speed('fastest')


def multiple_star():
    for _ in range (1):

        tim.forward(200)
        tim.left(115)
        tim.forward(100)
        tim.left(115)
        tim.forward(50)
        tim.right(50)
        tim.forward(50)
        tim.right(50)
        tim.forward(50)
        tim.left(115)
        tim.forward(100)






num = 70
while num != 0:

    multiple_star()
    new_pointing = tim.heading() + 5
    tim.setheading(new_pointing)
    num -= 1



screen.exitonclick()
