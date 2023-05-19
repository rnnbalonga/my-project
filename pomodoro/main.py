from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    main_text.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer_start():
    global reps
    reps += 1

    # work_sec = WORK_MIN * 60
    # short_break_sec = SHORT_BREAK_MIN * 60
    # long_break_sec = LONG_BREAK_MIN * 60

    #TEST CASE
    work_sec = 25
    short_break_sec = 5
    long_break_sec = 10

    #Set countdown value depending on number of reps
    if reps % 8 == 0:
        countdown(long_break_sec)
        main_text.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        main_text.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        main_text.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    #Calculate minutes and seconds
    #Read up on math.floor()
    count_min = math.floor(count / 60)
    count_sec = count % 60
    #Dynamically change seconds
    if count_sec < 10:
         count_sec = f"0{count_sec}"
    elif count_sec == 00:
         count_sec == "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
            global timer
            timer = window.after(1000, countdown, count - 1)
    else: 
        timer_start()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for num in range(work_sessions):
            marks += "✓"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Main Text
main_text = Label()
main_text.config(text="Timer", font=("Courier",56), bg=YELLOW, fg=GREEN)
main_text.grid(column=1, row=0)


#Create canvas
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
#Grab tomato photo
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=("Arial", 24))
canvas.grid(column=1, row=1)

#Start Button
start = Button()
start.config(text="Start", font=("Arial", 10), command=timer_start)
start.grid(column=0, row=2)

#Reset Button
reset = Button()
reset.config(text="Reset", font=("Arial", 10), command=timer_reset)
reset.grid(column=2, row=2)

#Checkmarks
checkmark = Label()
checkmark.config(text="", bg=YELLOW, fg=GREEN, font=("Arial", 12))
checkmark.grid(column=1, row=3)

window.mainloop()