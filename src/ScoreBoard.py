from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
file_name = "snake-score.txt"


def save_score(score):
    with open(file_name, mode="w") as file:
        file.write(str(score))


def get_high_score():
    try:
        with open(file_name) as file:
            score = int(file.read())
            return score
    except FileNotFoundError as e:
        save_score(0)
        return 0


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.penup()
        self.color("white")
        self.sety(415)
        self.hideturtle()
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            save_score(self.high_score)
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", False, align=ALIGNMENT, font=FONT)
