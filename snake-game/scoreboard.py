from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        #initialize superclass
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align=ALIGN, font = FONT)

   

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()
