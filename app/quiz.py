from .trivia import Question
class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    
    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            if question.difficulty == "Fácil":
                self.score += 1
            elif question.difficulty == "Media":
                self.score += 2
            elif question.difficulty == "Difícil":
                self.score += 3
            return True
        else:
            self.incorrect_answers += 1
            return False
    def get_points_for_question(self, question):
        if question.difficulty.lower() == "fácil":
            return 1
        elif question.difficulty.lower() == "media":
            return 2
        elif question.difficulty.lower() == "difícil":
            return 3
        return 0
