import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


#Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Set up Player
player = Player()

#Set up keypress to move the player up and down
screen.listen()

screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

#Set up Cars
car = CarManager()
car.start_point()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if player.ycor() > 240:
        player.start_pos()
   

    

#Create Turtle
#   Starts at the middle of the screen
#   Will only go along the y-axis. User clicks up to go up and down to go down
#   Will go back to the original starting position when it gets to the edge of the screen

#Create Cars
#   Random Turtle
#   All fixed size - think of paddle from Pong project
#   random colors
#   Will randomly be generated in the middle of the screen
#   Will move along the x-axis
#   Will double in speed every time turtle hits the top of the screen

#Screen
#   Will indicate which level user is currently in
#   Level will update every time turtle hits the top edge of the screen
#   Game will end once turtle gets hit by a car.
#   Shows 'Game Over' message once game ends as stated above