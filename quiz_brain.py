import html

# Class that handles the quiz logic
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # Check if there are still questions left in the list of questions
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Get the next question, formats it and update question number.
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # Unescape HTML entities
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    # Check the user's answer and update score
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False