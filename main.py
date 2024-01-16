from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
all_turtles = []
x_cords = [(0,0), (-20,0), (-40,0)]
for segment in range(0, 3):
    new_segment = Turtle()
    new_segment.speed("fastest")
    new_segment.penup()
    new_segment.shape("square")
    new_segment.goto(x_cords[segment])
    new_segment.color("white")
    all_turtles.append(new_segment)

screen.exitonclick()
