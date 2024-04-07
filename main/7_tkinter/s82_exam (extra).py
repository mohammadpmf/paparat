from tkinter import *
from tkinter import ttk, messagebox as msb

class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer = correct_answer

questions_easy = [
    Question("Where is The Capital of Iran?", "Rasht", "Tehran", "Isfahan", "Mashhad", "Tehran"),
    Question("Where is The Capital of England?", "Moscow", "Rome", "Berlin", "London", "London"),
    Question("Where is The Capital of France?", "Sen", "Paris", "Horizon", "Reno", "Paris"),
    Question("Where is The Capital of Italy?", "Vatikan", "Sisil", "Rome", "Madrid", "Rome"),
    Question("Where is The Capital of Germany?", "Eshtootgart", "Berlin", "Oslo", "Moonikh", "Berlin"),
]

questions_medium = [
    Question("Where is The Capital of The USA?", "Washington DC", "Los Santos :D", "Los Angeles", "California", "Washington DC"),
    Question("Where is The Capital of Canada?", "Ottawa", "Toronto", "Montreal", "Virginia", "Ottawa"),
    Question("Where is The Capital of Australia?", "Canberra", "Sydney", "Melbourne", "Packitow", "Canberra"),
    Question("Where is The Capital of Austria?", "Vienna", "Budapest", "Prauge", "Oslo", "Vienna"),
    Question("Where is The Capital of Argentina?", "Rashina", "Rio", "Arginia", "Boines Aires", "Boines Aires"),
]

questions_hard = [
    Question("Where is The Capital of The Togo?", "Kinshasa", "Karafia", "Lomé", "Barticia", "Lomé"),
    Question("Where is The Capital of Niger?", "Abuja", "Niamey", "Lome", "Harare", "Niamey"),
    Question("Where is The Capital of South Aferica?", "Pretoria", "Cape Town", "Bloemfontein", "All of them", "All of them"),
    Question("Where is The Capital of Philippines?", "Manila", "Varsu", "Prauge", "Adiss Ababa", "Manila"),
    Question("Where is The Capital of Trinidad and Tobago?", "Rojandi", "Rio", "Port of Spain", "Port of Madrid", "Port of Spain"),
]

BG = 'light blue'
FG = 'brown'
CNF_BTN = {
    'bg': BG,
    'fg': FG,
    'font': ('Calibri', 24),
    'padx': 10,
    'pady': 5
}
CNF_LABEL = {
    'bg': BG,
    'fg': FG,
    'font': ('Calibri', 24),
    'padx': 10,
    'pady': 5
}
CNF_RADIO = {
    'bg': BG,
    'fg': FG,
    'font': ('Calibri', 24),
    'padx': 10,
    'pady': 5
}
CNF_GRID = {
    'padx': 10,
    'pady': 5
}

def send():
    msb.showinfo("Grade", f"Your grade is {grade}/{len(questions)}")
    root.destroy()

def next_question(index):
    global questions, grade
    if sv.get() == questions[index].correct_answer:
        grade += 1
    if index == len(questions)-1:
        send()
        return
    index += 1
    lbl_question.config(text=questions[index].question)
    a1 = questions[index].answer1
    a2 = questions[index].answer2
    a3 = questions[index].answer3
    a4 = questions[index].answer4
    rb1.config(text=a1, value=a1, command=lambda:next_question(index))
    rb2.config(text=a2, value=a2, command=lambda:next_question(index))
    rb3.config(text=a3, value=a3, command=lambda:next_question(index))
    rb4.config(text=a4, value=a4, command=lambda:next_question(index))

def start():
    global questions
    combo_difficulty.grid_forget()
    btn_start.grid_forget()
    difficulty = combo_difficulty.get()
    if difficulty=='easy':
        questions = questions_easy.copy()
    elif difficulty=='normal':
        questions = questions_medium.copy()
    elif difficulty=='hard':
        questions = questions_hard.copy()
    index = 0
    lbl_question.config(text=questions[index].question)
    a1 = questions[index].answer1
    a2 = questions[index].answer2
    a3 = questions[index].answer3
    a4 = questions[index].answer4
    rb1.config(text=a1, value=a1, command=lambda:next_question(index))
    rb2.config(text=a2, value=a2, command=lambda:next_question(index))
    rb3.config(text=a3, value=a3, command=lambda:next_question(index))
    rb4.config(text=a4, value=a4, command=lambda:next_question(index))
    lbl_question.grid(row=1, column=1, columnspan=4, sticky='w')
    rb1.grid(row=2, column=1, sticky='w')
    rb2.grid(row=2, column=2, sticky='w')
    rb3.grid(row=2, column=3, sticky='w')
    rb4.grid(row=2, column=4, sticky='w')

grade = 0
root = Tk()
root.config(bg=BG)
combo_difficulty = ttk.Combobox(root, values=['easy', 'normal', 'hard'])
combo_difficulty.insert(0, 'normal')
combo_difficulty.config(state='readonly')
combo_difficulty.grid()
btn_start = Button(root, text='Start', cnf=CNF_BTN, command=start)
btn_start.grid()
lbl_question = Label(root, cnf=CNF_LABEL)
sv = StringVar(root)
sv.set("alaki")
rb1 = Radiobutton(root, cnf=CNF_RADIO, variable=sv)
rb2 = Radiobutton(root, cnf=CNF_RADIO, variable=sv)
rb3 = Radiobutton(root, cnf=CNF_RADIO, variable=sv)
rb4 = Radiobutton(root, cnf=CNF_RADIO, variable=sv)

root.mainloop()

