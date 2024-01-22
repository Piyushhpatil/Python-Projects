from question_model import Question
from data import question_data

question_bank = []

for questions in question_data:
    question_text = questions["text"]
    questions_answer = questions["answer"]
    new_question = Question(question_text, questions_answer)
    question_bank.append(new_question)
