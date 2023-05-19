from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Add Main Text
main_text = Label()
main_text.config(text="Timer", font=("Courier",56), bg=YELLOW, fg=GREEN)
main_text.pack()


#Create canvas
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
#Grab tomato photo
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="white", font=("Arial", 24))
canvas.pack()



window.mainloop()