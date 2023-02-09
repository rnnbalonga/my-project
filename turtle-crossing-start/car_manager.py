from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
CAR_END: -310

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(COLORS[random.randrange(0,5)])
        self.turtlesize(1,2,0)
        self.car_speed = STARTING_MOVE_DISTANCE
        self.penup()
        self.setheading(180)

    def start_point(self):
        """
        This function will set the starting point of the car.
        """
        self.setposition(random.randrange(-300,300),random.randrange(-210,230))

    def go_right(self):
        """
        This function will make the car who reaches CAR_END go back to RIGHT_HAND_START (or the right side of the screen).
        """
        self.goto(300,random.randrange(-210,230))
    
    def move(self):
        """
        Make the car move along the x-axis with STARTING_MOVE_DISTANCE.
        """
        self.forward(self.car_speed)

    def increase_speed(self):
        """
        Increase speed of the cars once player moves to the next level.
        """
        self.car_speed += MOVE_INCREMENT
        self.forward(self.car_speed)