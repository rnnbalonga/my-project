import colorgram
import random
from PIL import Image
import turtle as t

color = colorgram.extract('stardew-valley.jpg' ,10)

color_list = [(233, 169, 39), (157, 91, 35), (176, 160, 34), (88, 180, 42), (46, 132, 39), (8, 58, 22), (75, 34, 16), (17, 98, 22), (186, 222, 65)]


t.colormode(255)

jimmy_turtle = t.Turtle()
jimmy_turtle.penup()


def make_row(num_dots):
    """
    Draw number of dots in a single row. 
    """
    for number in range (num_dots):
        jimmy_turtle.dot(20, random.choice(color_list))
        jimmy_turtle.fd(50)
     
y_axis = -270

for i in range (10):
    jimmy_turtle.goto(-300, y_axis)
    y_axis += 50
    make_row(10)


from turtle import Screen
screen = Screen()
screen.exitonclick()


  
