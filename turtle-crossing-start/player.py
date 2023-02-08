from turtle import Turtle
import random

STARTING_POSITION = (0, -240)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 240

class Player(Turtle):

    #Initialize Class Player
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.start_pos()
    
    def move_up(self):
        """
        This function will make the player move 10 steps forward.
        """
        self.forward(MOVE_DISTANCE)

    
    def move_down(self):
        """
        This function will make the player move 10 steps backward.
        """
        self.forward(MOVE_DISTANCE * - 1)

    def start_pos(self):
        """
        This function will make the Player go back to the starting position.
        """
        if self.ycor == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
    

