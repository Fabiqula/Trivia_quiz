class QuizBrain:
    def __init__(self, question_library):
        self.question_number = 0
        self.score = 0
        self.question_list = question_library

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True/False or Answer: ")