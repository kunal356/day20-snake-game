from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()

game_is_on = True
while game_is_on:
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.right, key="Right")
    screen.onkey(fun=snake.left, key="Left")
    time.sleep(0.1)
    screen.update()
    snake.move()

screen.exitonclick()
