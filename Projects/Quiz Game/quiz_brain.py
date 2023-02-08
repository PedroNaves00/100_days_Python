class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.q_text} (True/False): ")
        self.chek_answer(user_answer, current_question.q_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def chek_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Your answer is right!")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}")
            print("\n")




