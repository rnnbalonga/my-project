from tkinter import * 
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

#------ FUNCTIONALITY ------#

df = pd.read_csv('data/french_words.csv')
learning_keywords = df.to_dict(orient="records")

# print(keywords)

#Randomize word

def random_word():
    guess_word = random.choice(learning_keywords)
    canvas.itemconfig(card_word, text=guess_word['French'])


#------ GUI ------#

#Window
window = Tk()
window.config(padx=20, pady=20, background=BACKGROUND_COLOR)
window.title("Memory Trainer")

#Canvas
canvas = Canvas(width=800, height=526)
canvas.grid(row=0,column=0, columnspan=2)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file='images/card_back.png')
canvas.create_image(400, 263, image=front_card_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 10, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold") )


#Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image)
wrong_button.grid(row=1,column=0)
wrong_button.config(highlightthickness=0, command=random_word)


#Check Button
check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image)
check_button.grid(row=1,column=1)
check_button.config(highlightthickness=0, command=random_word)

random_word()

window.mainloop()