from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect food contact
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()

    #detect collitision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or \
            snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    #detect collision with tail
    for segment in snake.square_objects[1:0]: #slice
        # if segment == snake.head:
        #     print(snake.head)
        #     print(segment)
        #     pass
        # elif snake.head.distance(segment) < 10:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
