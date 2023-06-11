from tkinter import *

THEME_COLOR = "#375362"

class QuizUI:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.minsize(width=320,height=500)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: ", font=("Arial", 12), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=2, column=0, columnspan=2)
        self.canvas.config(bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,150, text="hey", font=("Arial", 20, "italic"))

        self.window.mainloop()