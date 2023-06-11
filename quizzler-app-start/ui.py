from tkinter import *

THEME_COLOR = "#375362"

class QuizUI:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR)
        self.window.mainloop()