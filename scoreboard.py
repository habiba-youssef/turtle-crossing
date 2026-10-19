from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.penup()
        self.color("black")
        self.goto(-290,260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align='center', font=FONT)

