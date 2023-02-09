from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_END: -310
RIGHT_HAND_START = 300

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

    def go_right(self):
        """
        This function will make the car who reaches CAR_END go back to RIGHT_HAND_START (or the right side of the screen).
        """
        if self.xcor == CAR_END:
            self.goto(RIGHT_HAND_START,random.randrange(-220,230))