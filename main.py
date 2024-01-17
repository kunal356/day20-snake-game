from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.right, key="Right")
    screen.onkey(fun=snake.left, key="Left")
    time.sleep(0.1)
    screen.update()
    snake.move()
    # Collision detection with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()
    # Collision detection with wall
    if abs(snake.head.xcor()) > 280 or snake.head.ycor() > 280:
        game_is_on = False
        scoreboard.game_over()
    # Collision detection with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
