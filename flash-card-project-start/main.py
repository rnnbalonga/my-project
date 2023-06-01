from tkinter import * 
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

#------ FUNCTIONALITY ------#
if os.path.isfile('data/words_to_learn.csv'):
    df = pd.read_csv('data/words_to_learn.csv')
else:
    df = pd.read_csv('data/french_words.csv')
learn_keywords = df.to_dict(orient="records")
current_card = {}

# print(keywords)

#Randomize word

def random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(learn_keywords)
    canvas.itemconfig(card_word, text=current_card['French'])
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_side, image=front_card_image)
    flip_timer = window.after(3000, flip_card)
    remove_word()

def flip_card():
    canvas.itemconfig(card_side, image=back_card_image)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card['English'])

def remove_word():
    learn_keywords.remove(current_card)
    df = pd.DataFrame(learn_keywords)
    df.to_csv('data/words_to_learn.csv', index=False)
    

#Window
window = Tk()
window.config(padx=20, pady=20, background=BACKGROUND_COLOR)
window.title("Memory Trainer")
flip_timer = window.after(3000, flip_card)


#Canvas
canvas = Canvas(width=800, height=526)
canvas.grid(row=0,column=0, columnspan=2)
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file='images/card_back.png')
card_side = canvas.create_image(400, 263, image=front_card_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 20, "italic"))
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