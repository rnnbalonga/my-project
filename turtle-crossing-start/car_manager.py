from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(COLORS[random.randrange(0,5)])
        self.turtlesize(1,3,0)
        self.penup()
        self.setheading(180)

    def start_point(self):
        """
        This function will set the starting point of the car.
        """
        self.setposition(random.randrange(-300,300),random.randrange(-220,230))

