from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 14, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(0, 280)
        self.clear()
        self.write(f"Score: {self.score}", True, align=ALIGN, font= FONT)

    def add_score(self):
        self.score += 1
        self.update_score()