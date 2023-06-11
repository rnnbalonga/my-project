from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0/10", font=("Arial", 12), bg=THEME_COLOR, fg="white")
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
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}/10")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed all the questions! Your final score is {self.quiz.score}.")
            self.check_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    
    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="light green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
        