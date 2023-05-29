from tkinter import * 

BACKGROUND_COLOR = "#B1DDC6"

#------ GUI ------#

#Window
window = Tk()
window.config(padx=20, pady=20, background=BACKGROUND_COLOR)
window.title("Memory Trainer")

#Canvas
canvas = Canvas(width=800, height=526)
canvas.grid(row=0,column=0, columnspan=2)
front_card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)

#Title Text
title = Label()
title.place(x=400,y=150)
title.config(text="Sample Text", font=("Arial", 10, "italic"))

#Word Text
word = Label()
word.place(x=-400,y=263)
word.config(text="Sample Text", font=("Arial", 60, "bold"))


#Wrong Button
wrong_button = Button()
wrong_button.grid(row=1,column=0)


#Check Button
check_button = Button()
check_button.grid(row=1,column=1)


window.mainloop()