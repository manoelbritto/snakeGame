from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 14, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.high_score = 0
        self.score = 0
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(0, 280)
        self.clear()
        self.write(f"Score:   {self.score}   High score:   {self.high_score}", True, align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", True, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()
