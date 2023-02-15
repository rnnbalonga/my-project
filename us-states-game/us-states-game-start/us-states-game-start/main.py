import turtle
import pandas

#Screen Set Up
screen = turtle.Screen()
screen.title("U.S. States Game")

#Set up image as background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Set up getting coordinates via mouseclick on screen
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)


screen.mainloop()

