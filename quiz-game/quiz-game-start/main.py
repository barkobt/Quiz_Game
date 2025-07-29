from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for item in question_data:
    list_item = Question(item["text"],item["answer"])
    question_bank.append(list_item)

quiz = QuizBrain(question_bank)



while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz.")
print(f"You're final score: {quiz.score}/{quiz.question_number}")

        

