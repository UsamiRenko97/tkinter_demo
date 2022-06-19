import tkinter
from tkinter import ttk
from tkinter import messagebox
import random


def main():
    root = tkinter.Tk()
    root.title('Multiply Test')
    root.geometry('520x400')

    frame = ttk.Frame(root, padding=10)
    frame.grid()

    title_label = ttk.Label(frame, text='Welcome to Multiply Test', padding=10, font=('Times', 20, 'bold'))
    title_label.grid(columnspan=6)

    row = 1
    text = ['No', 'Name']
    for i in range(2):
        label_entry = LabelEntry(frame, text[i], row, 3 * i)
        label_entry.grid()
        entry_examiner.register(label_entry.entry, "Please enter your student number and name")

    row = row + 1
    ttk.Label(frame, padding=15).grid(row=row, columnspan=6)

    for i in range(5):
        row = row + 1
        for j in range(2):
            index = 2 * i + j + 1
            col = 3 * j
            question_widget = QuestionWidget(frame, index, row, col)
            question_widget.grid()
            entry_examiner.register(question_widget.entry, "Please enter the answer of Q" + str(index))
            question_examiner.register(question_widget.entry,
                                       Question(question_widget.number1, question_widget.number2))

    submit_button = ttk.Button(frame, text='Submit', command=lambda: entry_examiner.examine())
    submit_button.grid()

    root.mainloop()


# combine one ttk.Label and one ttk.Entry
class LabelEntry:

    def __init__(self, master, name, row, col):
        self.label = ttk.Label(master, text=name + ':', justify='left', width=5, padding=5)
        self.entry = ttk.Entry(master, justify='left', width=15)
        self.row = row
        self.col = col

    def grid(self):
        self.label.grid(columnspan=2, column=self.col, row=self.row)
        self.entry.grid(column=self.col + 2, row=self.row)


# the multiply question class
class QuestionWidget:

    def __init__(self, master, index, row, col):
        self.number1 = random.randint(1, 9)
        self.number2 = random.randint(1, 9)
        question = 'Q' + str(index) + '.  ' + str(self.number1) + ' * ' + str(self.number2) + ' = '
        self.label = ttk.Label(master, text=question, justify='left', padding=5)
        self.entry = ttk.Entry(master, justify='left', width=15)
        self.row = row
        self.col = col

    def grid(self):
        self.label.grid(columnspan=2, row=self.row, column=self.col)
        self.entry.grid(row=self.row, column=self.col + 2)


# base class of examiner
class Examiner:
    # the ttk.Entries to be examined
    entries = []
    # something helpful when examine
    helpers = []

    # register a ttk.Entry to the Examiner
    def register(self, entry, helper):
        self.entries.append(entry)
        self.helpers.append(helper)


# examine if the ttk.Entries are filled
class EntryExaminer(Examiner):

    def examine(self):
        for i in range(len(self.entries)):
            if self.entries[i].get() == "":
                messagebox.showwarning('Warning', self.helpers[i])
                return
        # if all entries are filled, check whether the answers are correct
        question_examiner.examine()


class Question:
    num1 = 0
    num2 = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def product(self):
        return self.num1 * self.num2


class QuestionExaminer(Examiner):
    score = 0

    # if one question correctly answered, score will add 10
    def examine(self):
        for i in range(len(self.entries)):
            if isinstance(self.helpers[i], Question) and self.helpers[i].product() == int(self.entries[i].get()):
                self.score = self.score + 10

        msg = 'You got ' + str(self.score) + ' in this examination. '
        if self.score <= 50:
            messagebox.showwarning('Fail', msg + 'You did not pass!')
        elif self.score <= 90:
            messagebox.showinfo('Pass', msg + 'You passed the exam, but not perfect~')
        else:
            messagebox.showinfo('Perfect', msg + 'Congratulations! You got a perfect score!')


entry_examiner = EntryExaminer()
question_examiner = QuestionExaminer()
main()
