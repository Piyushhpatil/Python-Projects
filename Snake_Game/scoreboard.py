from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.highscores = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"score: {self.scores} High Score: {self.highscores}", align="center", font=("Arial", 15, "normal"))

    def reset_game(self):
        if self.scores > self.highscores:
            self.highscores = self.scores
        self.scores = 0
        self.update()

    def increase_score(self):
        self.scores += 1
        self.update()
