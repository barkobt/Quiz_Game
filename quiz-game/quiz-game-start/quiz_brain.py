class QuizBrain:

    

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} True or False?: ")
        self.check_answer(user_answer,current_question.answer) 

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it! Current score: {self.score}")

        else: 
            print(f"You lost! Final score: {self.score}")
        print(f"The correct answer was: {correct_answer}")
        print(f"You're current score is {self.score}/{self.question_number}")
        print("\n")
        



    
        
    
        
            
    # question_list = []
    # question_number = 0
    # answer_list = []

    # for item in question_bank:
    #     question_list.append(item.text)
    #     answer_list.append(item.answer)


    # isTrue = True   
    # while isTrue:
    #     tf = input(f"{question_list[question_number]} True or False?: ")
    #     if tf.lower() == answer_list[question_number].lower():
    #         question_number += 1
    #         print(f"You got it! Current score: {question_number}")
    #     else:
    #         isTrue = False
    #         print(f"You lost! Your final score: {question_number}")





    

    



        