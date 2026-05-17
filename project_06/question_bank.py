from questions_data import questions


class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class QuestionBank:
    def __init__(self):
        question_bank = []
        for question in questions:
            question_bank.append(
                Question(question["question"], question["correct_answer"])
            )
        self.questions = question_bank
