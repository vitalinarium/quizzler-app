from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizUi:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score', bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.ques_text = self.canvas.create_text(150, 125, width=280, text='Quiz question', fill=THEME_COLOR,
                                                 font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_button = Button(command=self.true_pressed)
        true_img = PhotoImage(file='images/true.png')
        self.true_button.config(image=true_img)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(command=self.false_pressed)
        false_img = PhotoImage(file='images/false.png')
        self.false_button.config(image=false_img)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():

            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=q_text)
        else:
            self.canvas.itemconfig(self.ques_text, text='You`ve reached the end of the quiz')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

