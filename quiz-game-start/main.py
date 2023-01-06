from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#This is what we will use to create a list of questions for the quiz.
question_bank = []

#Create questions based on the contents of question_data.
for question in question_data:
    #Get question_text from the list of dictionaries in question_data.
    question_text = question['question']
    #Get the correct answer from the list of dictionaries in question_data.
    question_answer = question['correct_answer']
    #Create a new question using the class Question which captures the question_text & question_answer.
    new_question = Question(question_text, question_answer)
    #Append the created question to the question_bank list.
    question_bank.append(new_question)

#Create an object 'quiz' using the QuizBrain class which requires a list of questions (question_bank) as an argument.
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    answer = quiz.next_question()

print("Game Over")
print(f"Your score is {quiz.score}/{len(question_bank)}")