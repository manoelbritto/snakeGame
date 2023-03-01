from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("My Snake Game")

square_objects = []
x_position = 0
for _ in range (3):
    square = Turtle()
    square.shape("square")
    square.color("white")
    square.setposition(x_position, 0)
    x_position -= 20
    square_objects.append(square)

print (square_objects)
screen.exitonclick()