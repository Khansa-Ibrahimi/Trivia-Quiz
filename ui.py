THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

# Class to handle the GUI
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Setup window
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Load button images
        self.true_pic = PhotoImage(file="images/true.png")
        self.false_pic = PhotoImage(file="images/false.png")

        # Score display
        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=1, column=2)

        # Canvas to display the question
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Something",
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        # True/False buttons
        self.true_button = Button(image=self.true_pic, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=3, column=1)
        self.false_button = Button(image=self.false_pic, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=3, column=2)

        self.get_next_question()

        self.window.mainloop()

    # Load the next question or end quiz
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():  # <- FIXED
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.canvas.config(bg="green" if is_right else "red")
        self.window.after(1000, self.get_next_question)
