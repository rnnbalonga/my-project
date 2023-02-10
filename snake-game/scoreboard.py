from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        #initialize superclass
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt","w") as data:
                data.write(f"{self.high_score}")
            self.score = 0
            self.clear()
            self.update_score()   

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over!", align=ALIGN, font = FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()
