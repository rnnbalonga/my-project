from turtle import Turtle

FONT = ("Courier", 24, "normal")


ALIGN = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        #initialize superclass
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-270,270)
