from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        #initialize superclass
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-270,270)
        self.hideturtle()
