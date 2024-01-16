from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

all_segments = []
x_cords = [(0, 0), (-20, 0), (-40, 0)]
for segment in range(0, 3):
    new_segment = Turtle()
    new_segment.speed("fastest")
    new_segment.penup()
    new_segment.shape("square")
    new_segment.goto(x_cords[segment])
    new_segment.color("white")
    all_segments.append(new_segment)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(all_segments)-1,0, -1):
        new_x_cord = all_segments[seg_num - 1].xcor()
        new_y_cord = all_segments[seg_num - 1].ycor()
        all_segments[seg_num].goto(new_x_cord, new_y_cord)
    all_segments[0].forward(20)
screen.exitonclick()
