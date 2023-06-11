from tkinter import *

THEME_COLOR = "#375362"

class QuizUI:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.minsize(width=400,height=600)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: ", font=("Arial", 12), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)


        self.window.mainloop()