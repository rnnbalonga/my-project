import turtle
import pandas

#Screen Set Up
screen = turtle.Screen()
screen.title("U.S. States Game")

#Set up image as background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")
states_list = df.state.to_list()
#Create list of the states correctly guessed by user
user_guess = []

#Keep the screen open while guessed states < 50
while len(user_guess) < 50:
    answer_state = screen.textinput(title=f"{len(user_guess)}/50 States Correct", prompt="What's another state's name?").title()

    #Create mechanism to force end game
    if answer_state == "Exit":
        #Get the difference between the states_list and user_guess
        unmemorized_states = list(set(states_list) - set(user_guess))
        df_new = pandas.DataFrame(unmemorized_states)
        df_new.to_csv("Unmemorized States")
        break
    if answer_state in states_list:
        #Append correct answer to user_guess
        user_guess.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #Grab row data
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    

print(type(unmemorized_states))


#Set up getting coordinates via mouseclick on screen
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)


# screen.mainloop()

