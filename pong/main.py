from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

#Create Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pongertz")
screen.tracer(0)

#Set up left & right paddles
left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))

#Set up Ball
ball = Ball()

#Set up Scoreboard
score = Scoreboard()

#Set up keypress to move paddles up and down along the y-axis
screen.listen()

screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")


#Game mode 
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when player misses

    if ball.xcor() > 380:
        ball.reset()
        score.left_point()

    elif ball.xcor() < -380:
        ball.reset()
        score.right_point()

screen.exitonclick()