from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment in range(0, 3):
            self.add_segment(STARTING_POSITION[segment])

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.speed("fastest")
        new_segment.penup()
        new_segment.shape("square")
        new_segment.goto(position)
        new_segment.color("white")
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_cord = self.segments[seg_num - 1].xcor()
            new_y_cord = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_cord, new_y_cord)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
