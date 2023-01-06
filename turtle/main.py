import random
import turtle as t

jim_turtle = t.Turtle()

jim_turtle.shape("turtle")
jim_turtle.color("green")
jim_turtle.speed(0)
t.colormode(255) 

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r, g, b)


def draw_polygon(num_sides):
    angle = 360 / num_sides

    for i in range (num_sides):
        jim_turtle.forward(50)
        jim_turtle.right(angle)
        

for polygon_sides in range (3,11):
    draw_polygon(polygon_sides)
    jim_turtle.color(random_color())

# def random_walk():
#     jim_turtle.color(random_color())
#     jim_turtle.forward(50)
#     random_face_direction()

    
# def random_face_direction():
#     angle = random.choice([0,90,180,270])
#     jim_turtle.setheading(angle)

# for i in range (100):
#     random_walk()

# for i in range(72):
#     jim_turtle.color(random_color())
#     jim_turtle.circle(100)
#     heading_start = jim_turtle.heading()
#     move_heading = jim_turtle.setheading(heading_start + 5)
    


from turtle import Screen
screen = Screen()
screen.exitonclick()