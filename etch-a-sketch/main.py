from turtle import Turtle, Screen

jimmy_turtle = Turtle()



def move_forward():
    jimmy_turtle.forward(10)

def move_backward():
    jimmy_turtle.backward(10)

def turn_clockwise():
    jimmy_turtle.left(-5)

def turn_counter_clockwise():
    jimmy_turtle.right(-5)

def clear():
    jimmy_turtle.clear()
    jimmy_turtle.penup()
    jimmy_turtle.home()
    jimmy_turtle.pendown()

screen = Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkeypress(key="a", fun=turn_counter_clockwise)
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()