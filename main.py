from question_model import Questions
from data import question_data

question_lib = []
for questions in question_data:
    question_text = questions["question"]

    question_answer = questions["correct_answer"]

    new_question = Questions(question_text, question_answer)
    question_lib.append(new_question)


