from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.penup()
        self.goto(0,0)
        self.rand_dir = [-10,10]
        self.rand_x_start = random.choice(self.rand_dir)
        self.rand_y_start = random.choice(self.rand_dir)
        self.x_move = self.rand_x_start
        self.y_move = self.rand_y_start
        self.move_speed = 0.1

    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.5
    
    
    def reset(self):
        self.move_speed = 0.1
        self.goto(0,0)

