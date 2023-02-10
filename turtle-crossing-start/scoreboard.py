from turtle import Turtle

FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        #initialize superclass
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        #Set spawn point
        self.goto(-270,260)
        self.hideturtle()
        self.level = 1

    def start_level(self):
        """
        This function will write the player level in the screen.
        """
        self.write(f"Current level: {self.level}",font= FONT)

    def update_level(self):
        """
        This function will update the level of the player.
        """
        self.level += 1
        self.start_level()
    
    def game_over(self):
        """
        Make the scoreboard appear in the center and then write the game over text.
        """
        self.goto(-20,0)
        self.write(f"GAME OVER.\nYour score is: {self.level}",align = "center",font= FONT)