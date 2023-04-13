from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.square_objects = []
        self.create_snake()
        self.head = self.square_objects[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        square = Turtle()
        square.shape("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.square_objects.append(square)

    def extend(self):
        self.add_segment(self.square_objects[-1].position())

    def move(self):
        for seg_num in range(len(self.square_objects) - 1, 0, -1):
            new_x = self.square_objects[seg_num - 1].xcor()
            new_y = self.square_objects[seg_num - 1].ycor()
            self.square_objects[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset (self):
        for seg in self.square_objects:
            seg.goto(1000,1000)
        self.square_objects.clear()
        self.create_snake()
        self.head = self.square_objects[0]