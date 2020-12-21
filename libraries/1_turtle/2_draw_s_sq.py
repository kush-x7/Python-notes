from turtle import Turtle, Screen

t_obj = Turtle()
t_obj.shape("turtle")
t_obj.color("red")

for _ in range (4):
    t_obj.forward(10)
    t_obj.right(90)




screen_obj= Screen()

screen_obj.exitonclick()
