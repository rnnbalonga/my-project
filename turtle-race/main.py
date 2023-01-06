from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=500)
user_bet = screen.textinput(title="Place your bet!", prompt="Select your winner: ")
colors = ["red", "orange", "yellow", "green", "blue"]
y_axis = [-100, -50, 0, 50, 100]
turtle_roster = []


for turtle_index in range (0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_axis[turtle_index])
    turtle_roster.append(new_turtle)


if user_bet:
    is_race_on = True

    while is_race_on:

        for turtle in turtle_roster:
            if turtle.xcor() > 220:
                winning_turtle = turtle.pencolor()
                is_race_on = False

                if user_bet == winning_turtle:
                    print("You've won!")
                else:
                    print("lmao")

            rand_steps = random.randint(0,10)
            turtle.forward(rand_steps)

screen.exitonclick()