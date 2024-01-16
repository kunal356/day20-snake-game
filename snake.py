from turtle import Turtle


class Snake:
    STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    def __init__(self):
        self.segments =[]
        self.create_snake()

    def create_snake(self):
        for segment in range(0, 3):
            new_segment = Turtle()
            new_segment.speed("fastest")
            new_segment.penup()
            new_segment.shape("square")
            new_segment.goto(self.STARTING_POSITION[segment])
            new_segment.color("white")
            self.segments.append(new_segment)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x_cord = self.segments[seg_num - 1].xcor()
            new_y_cord = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x_cord, new_y_cord)
        self.segments[0].forward(self.MOVE_DISTANCE)
