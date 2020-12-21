# import colorgram
#
# rgb_colors =[]
# colors = colorgram.extract('unnamed.jpg', 30)
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color= (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random

colors = [(231, 205, 85), (228, 148, 89), (230, 221, 226), (217, 226, 219), (120, 167, 186), (216, 222, 227), (162, 11, 19), (31, 111, 160), (234, 81, 45), (175, 19, 14), (124, 177, 145), (5, 99, 36), (189, 186, 23), (207, 65, 23), (26, 131, 43), (10, 40, 76), (243, 202, 5), (14, 63, 40), (86, 14, 22), (135, 84, 99), (48, 167, 74), (4, 65, 140), (173, 134, 149), (39, 22, 19), (49, 150, 195), (228, 171, 161), (219, 63, 69), (73, 134, 188)]

tim = turtle.Turtle()

tim.speed("fastest")
turtle.colormode(255)

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 180

for num in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.forward(50)

    if num %10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)







screen = turtle.Screen()
screen.exitonclick()




















 tim.setheading(270)
        tim.forward(200)
        tim.setheading(0)
        tim.forward(50)
        tim.setheading(90)
        tim.forward(50)

        tim.setheading(315)
        tim.forward(70)

        tim.setheading(90)
        tim.forward(50)

        tim.setheading(135)
        tim.forward(70)

        tim.setheading(45)
        tim.forward(70)

        tim.setheading(90)
        tim.forward(50)

        tim.setheading(225)
        tim.forward(70)

        tim.setheading(90)
        tim.forward(50)

        tim.setheading(180)
        tim.forward(50)
