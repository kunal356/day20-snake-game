from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.print_score()

    def reset_score(self):
        if self.score > self.high_score:
            with open("data.txt",mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.print_score()
