from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_board = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score_board()
        self.add_score()

    def update_score_board(self):
        self.write(f"Score  : {self.score_board - 1} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score_board += 1
        self.clear()
        self.update_score_board()
