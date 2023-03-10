from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.square_objects = []
        self.x_position = 0
        self.create_snake()
        self.head = self.square_objects[0]

    def create_snake (self):
        for _ in range(3):
            square = Turtle()
            square.shape("square")
            square.color("white")
            square.penup()
            square.setposition(self.x_position, 0)
            self.x_position -= 20
            self.square_objects.append(square)

    def move (self):
        for seg_num in range(len(self.square_objects) - 1, 0, -1):
            new_x = self.square_objects[seg_num - 1].xcor()
            new_y = self.square_objects[seg_num - 1].ycor()
            self.square_objects[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up (self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down (self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left (self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right (self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)