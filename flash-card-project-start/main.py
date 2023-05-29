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
canvas.create_text(400, 150, text="Title", font=("Arial", 10, "italic"))
canvas.create_text(-400, 263, text="Word", font=("Arial", 60, "bold") )

#Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image)
wrong_button.grid(row=1,column=0)
wrong_button.config(highlightthickness=0)


#Check Button
check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image)
check_button.grid(row=1,column=1)
check_button.config(highlightthickness=0)

window.mainloop()