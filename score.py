from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write("Score: ", True, align="center", font=('Arial', 14, 'normal'))
        self.write(self.score, True, font=('Arial', 14, 'normal'))

    def add_score(self):
        self.goto(0, 280)
        self.clear()
        self.score += 1
        self.write("Score: ", True, align="center", font=('Arial', 14, 'normal'))
        self.write(self.score, True, font=('Arial', 14, 'normal'))