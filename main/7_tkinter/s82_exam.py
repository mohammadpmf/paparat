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

def send():
    msb.showinfo("Grade", f"Your grade is {grade}/{len(questions)}")
    root.destroy()

def next_question(index):
    global questions, grade
    if sv.get() == questions[index].get('correct_answer'):
        grade += 1
    if index == len(questions)-1:
        send()
        return
    index += 1
    lbl_question.config(text=questions[index].get('question'))
    temp = questions[index].get('answers')
    rb1.config(text=temp[0], value=temp[0], command=lambda:next_question(index))
    rb2.config(text=temp[1], value=temp[1], command=lambda:next_question(index))
    rb3.config(text=temp[2], value=temp[2], command=lambda:next_question(index))
    rb4.config(text=temp[3], value=temp[3], command=lambda:next_question(index))

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
    lbl_question.config(text=questions[index].get('question'))
    temp = questions[index].get('answers')
    rb1.config(text=temp[0], value=temp[0], command=lambda:next_question(index))
    rb2.config(text=temp[1], value=temp[1], command=lambda:next_question(index))
    rb3.config(text=temp[2], value=temp[2], command=lambda:next_question(index))
    rb4.config(text=temp[3], value=temp[3], command=lambda:next_question(index))
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

