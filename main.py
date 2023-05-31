from question_model import Questions
from data import question_data
from brain import QuizBrain

question_lib = []
for questions in question_data:
    question_text = questions["question"]
    question_answer = questions["correct_answer"]
    new_question = Questions(question_text, question_answer)
    question_lib.append(new_question)

print(question_lib[0].answer)
quiz = QuizBrain(question_lib)
quiz.next_question()