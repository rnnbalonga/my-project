from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: ", font=("Arial", 12), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.canvas.config(bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 120, width=280, text="hey", font=("Arial", 18, "italic"))

        #Check Button
        self.check_image = PhotoImage(file="images/true.png")
        self.check_button = Button(image=self.check_image,command=self.answer_true)
        self.check_button.grid(row=2,column=0)
        self.check_button.config(highlightthickness=0)


        #Wrong Button
        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, command=self.answer_false)
        self.wrong_button.grid(row=2,column=1)
        self.wrong_button.config(highlightthickness=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    
    def answer_true(self):
        self.quiz.check_answer("True")
    
    def answer_false(self):
        self.quiz.check_answer("False")
