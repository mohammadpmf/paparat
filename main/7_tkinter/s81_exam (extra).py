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

def start():
    def send():
        grade = 0
        for index, question in enumerate(questions):
            if sv_list[index].get()==question.correct_answer:
                grade+=1                
        msb.showinfo("Grade", f"Your grade is {grade}/{len(questions)}")
        root.destroy()
    combo_difficulty.grid_forget()
    btn_start.grid_forget()
    difficulty = combo_difficulty.get()
    if difficulty=='easy':
        questions = questions_easy.copy()
    elif difficulty=='normal':
        questions = questions_medium.copy()
    elif difficulty=='hard':
        questions = questions_hard.copy()
    sv_list = []
    for row, question in enumerate(questions):
        sv_list.append(StringVar(root))
        Label(root, text=question.question, cnf=CNF_LABEL).grid(row=2*row, column=1, columnspan=4, sticky='w')
        sv_list[row].set('alaki')
        Radiobutton(root, text=question.answer1, variable=sv_list[row], value=question.answer1, cnf=CNF_RADIO).grid(row=2*row+1, column=1, sticky='w')
        Radiobutton(root, text=question.answer2, variable=sv_list[row], value=question.answer2, cnf=CNF_RADIO).grid(row=2*row+1, column=2, sticky='w')
        Radiobutton(root, text=question.answer3, variable=sv_list[row], value=question.answer3, cnf=CNF_RADIO).grid(row=2*row+1, column=3, sticky='w')
        Radiobutton(root, text=question.answer4, variable=sv_list[row], value=question.answer4, cnf=CNF_RADIO).grid(row=2*row+1, column=4, sticky='w')
    Button(root, text='Send', cnf=CNF_BTN, command=send).grid(row=1000, column=1)

root = Tk()
root.config(bg=BG)
combo_difficulty = ttk.Combobox(root, values=['easy', 'normal', 'hard'])
combo_difficulty.insert(0, 'normal')
combo_difficulty.config(state='readonly')
combo_difficulty.grid()
btn_start = Button(root, text='Start', cnf=CNF_BTN, command=start)
btn_start.grid()
root.mainloop()