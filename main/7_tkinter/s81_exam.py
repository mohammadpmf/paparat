from tkinter import *
from tkinter import ttk, messagebox as msb

questions_easy = [
    {
        "question": "Where is The Capital of Iran?",
        "answers": ["Rasht", "Tehran", "Isfahan", "Mashhad"],
        "correct_answer": "Tehran"
    },
    {
        "question": "Where is The Capital of England?",
        "answers": ["Moscow", "Rome", "Berlin", "London"],
        "correct_answer": "London"
    },
    {
        "question": "Where is The Capital of France?",
        "answers": ["Sen", "Paris", "Horizon", "Reno"],
        "correct_answer": "Paris"
    },
    {
        "question": "Where is The Capital of Italy?",
        "answers": ["Vatikan", "Sisil", "Rome", "Madrid"],
        "correct_answer": "Rome"
    },
    {
        "question": "Where is The Capital of Germany?",
        "answers": ["Eshtootgart", "Berlin", "Oslo", "Moonikh"],
        "correct_answer": "Berlin"
    }
]

questions_medium = [
    {
        "question": "Where is The Capital of The USA?",
        "answers": ["Washington DC", "Los Santos :D", "Los Angeles", "California"],
        "correct_answer": "Washington DC"
    },
    {
        "question": "Where is The Capital of Canada?",
        "answers": ["Ottawa", "Toronto", "Montreal", "Virginia"],
        "correct_answer": "Ottawa"
    },
    {
        "question": "Where is The Capital of Australia?",
        "answers": ["Canberra", "Sydney", "Melbourne", "Packitow"],
        "correct_answer": "Canberra"
    },
    {
        "question": "Where is The Capital of Austria?",
        "answers": ["Vienna", "Budapest", "Prauge", "Oslo"],
        "correct_answer": "Vienna"
    },
    {
        "question": "Where is The Capital of Argentina?",
        "answers": ["Rashina", "Rio", "Arginia", "Boines Aires"],
        "correct_answer": "Boines Aires"
    }
]

questions_hard = [
    {
        "question": "Where is The Capital of The Togo?",
        "answers": ["Kinshasa", "Karafia", "Lomé", "Barticia"],
        "correct_answer": "Lomé"
    },
    {
        "question": "Where is The Capital of Niger?",
        "answers": ["Abuja", "Niamey", "Lome", "Harare"],
        "correct_answer": "Niamey"
    },
    {
        "question": "Where is The Capital of South Aferica?",
        "answers": ["Pretoria", "Cape Town", "Bloemfontein", "All of them"],
        "correct_answer": "All of them"
    },
    {
        "question": "Where is The Capital of Philippines?",
        "answers": ["Manila", "Varsu", "Prauge", "Adiss Ababa"],
        "correct_answer": "Manila"
    },
    {
        "question": "Where is The Capital of Trinidad and Tobago?",
        "answers": ["Rojandi", "Rio", "Port of Spain", "Port of Madrid"],
        "correct_answer": "Port of Spain"
    }
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
            if sv_list[index].get()==question.get('correct_answer'):
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
        Label(root, text=question.get('question'), cnf=CNF_LABEL).grid(row=2*row, column=1, columnspan=4, sticky='w')
        for column, answer in enumerate(question.get('answers')):
            sv_list[row].set('alaki')
            Radiobutton(root, text=answer, variable=sv_list[row], value=answer, cnf=CNF_RADIO).grid(row=2*row+1, column=column+1, sticky='w')
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

