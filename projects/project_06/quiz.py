from projects.project_06.question_bank import QuestionBank


class Quiz:
    def __init__(self):
        question_bank = QuestionBank()
        self.questions = question_bank.questions
        self.score = 0
        self.current_question_idx = 0

    def show_score(self):
        return f"{self.score}/{len(self.questions)}"

    def performance_status(self):
        status = ""
        score_percentage = (self.score * 100) / len(self.questions)
        if score_percentage > 80:
            status = "Excellent"
        elif score_percentage > 60:
            status = "Good"
        elif score_percentage > 40:
            status = "Needs Improvement"
        else:
            status = "NEEDS SERIOUS ATTENTION"
        return status

    def get_question(self):
        current_question = self.questions[self.current_question_idx]
        self.current_question_idx += 1
        return f"{self.current_question_idx}). {current_question.question} [True/False] :\n"

    def has_remaining_questions(self):
        return self.current_question_idx < len(self.questions)

    def check_answer(self, user_answer):
        current_question = self.questions[self.current_question_idx - 1]
        self.score += 1 if current_question.answer == user_answer else 0
        return (
            "That's Correct"
            if current_question.answer == user_answer
            else "You got it Wrong"
        )

    def get_user_response(self, question, valid_values):
        valid_response = False
        response = False
        while not valid_response:
            response = input(question).strip()
            valid_response = True if response in valid_values else False
            if not valid_response:
                print(f"Enter valid value : {valid_values}")
        return response

    def start(self):
        print("QUIZ STARTED\n")
        try:
            while self.has_remaining_questions():
                user_response = self.get_user_response(
                    self.get_question(), ["True", "False"]
                )
                user_response_status = self.check_answer(user_response)
                user_score_now = self.show_score()
                print(f"{user_response_status}\nScore : {user_score_now}\n")
        except KeyboardInterrupt:
            print("QUIZ EXITED")
        else:
            print("QUIZ FINISHED")
        finally:
            print(f"Final Score : {self.show_score()} [{self.performance_status()}]")
