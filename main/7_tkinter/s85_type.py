from tkinter import *
import random
from threading import Thread
from time import sleep
from tkinter import messagebox as msb

BG='#333333'
FG='orange'
HINT_COLOR_DEFAULT = '#555555'
HINT_COLOR_WRONG = 'red'
HINT_COLOR_CORRECT = 'green'
LIMIT = 18
TIME=10
WORDS = ['red', 'green', 'blue', 'computer', 'cellphone', 'school', 'monitor', 'giraffe', 'mouse', 'keyboard','red', 'green', 'blue', 'computer', 'cellphone', 'school', 'monitor', 'giraffe', 'mouse', 'keyboard']

CNF_BTN = {
    'bg': BG,
    'fg': FG,
    'font': ('', 28),
    'padx': 10,
    'pady': 5
}
CNF_ENTRY = {
    'bg': BG,
    'fg': FG,
    'font': ('', 28),
    'insertbackground': FG,
}
CNF_LABEL = {
    'bg': BG,
    'fg': FG,
    'font': ('', 28),
    'padx': 10,
    'pady': 5,
    'justify': 'left',
}
CNF_GRID = {
    'padx': 20,
    'pady': 10,
}

def start_typing():
    global index, words, correct_words, wrong_words, is_started
    is_started=True
    sv_word.set(words[index])
    entry.focus_set()
    btn_start.config(state='disabled')
    time = TIME
    while time>0:
        time -= 1
        sleep(1)
        label_time.config(text=f"Ramaining time: {time}")
        root.title(f"Ramaining time: {time}")
    btn_start.config(state='normal')
    wpm = correct_words*60/TIME
    try:
        message = f"Correct Words: {correct_words}\nWrong Words: {wrong_words}\nAccuracy: {round(correct_words*100/(correct_words+wrong_words), 2)}%\nWPM: {wpm}"
    except ZeroDivisionError:
        message = "Correct Words: 0\nWrong Words: 0\nAccuracy: 0\nWPM: 0"
    msb.showinfo("Typing test finished", message)
    correct_words=0
    wrong_words=0
    index=0
    is_started=False
    label_time.config(text=f"Ramaining time: {TIME}")
    shuffle_words()
    label_words.config(text=words)
    sv_word.set(words[0])

def start():
    entry.delete(0, END)
    Thread(target=start_typing, daemon=True).start()

def space(event=None):
    global correct_words, wrong_words
    if entry.get() == sv_word.get():
        correct_words += 1
    else:
        wrong_words += 1

def check(event=None):
    global correct_words, wrong_words, words, index, is_started
    if is_started==False:
        Thread(target=start_typing, daemon=True).start()
    word1 = entry.get()
    word2 = sv_word.get()
    if  word1 == word2:
        label_word.config(bg=HINT_COLOR_CORRECT)
    else:
        try:
            for i, char in enumerate(word1):
                if char!=word2[i]:
                    label_word.config(bg=HINT_COLOR_WRONG)
                    break
                else:
                    label_word.config(bg=HINT_COLOR_DEFAULT)
        except IndexError:
            label_word.config(bg=HINT_COLOR_WRONG)

    if event.keysym=='space':
        entry.delete(0, END)
        index+=1
        if index==len(words):
            index=0
            shuffle_words()
            label_words.config(text=words)
        sv_word.set(words[index])
        label_word.config(bg=HINT_COLOR_DEFAULT)

def shuffle_words():
    global words
    words = WORDS
    random.shuffle(words)
    words = words[0:LIMIT]


is_started = False
correct_words = 0
wrong_words = 0
index=0
words=''
shuffle_words()

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{int(2*width/3)}x{int(2*height/3)}+{int(width/6)}+{int(height/6)}')
root.config(bg=BG)
label_words = Label(root, text=words, cnf=CNF_LABEL, wraplength=1200)
sv_word = StringVar(root)
sv_word.set(words[index])
label_word = Label(root, bg=HINT_COLOR_DEFAULT, cnf=CNF_LABEL, textvariable=sv_word)
entry = Entry(root, cnf=CNF_ENTRY)
entry.bind('<KeyRelease>', check)
entry.bind('<space>', space)
entry.focus_set()
btn_start = Button(root, text='Start', command=start, cnf=CNF_BTN)
label_time = Label(root, text=f"Ramaining time: {TIME}", cnf=CNF_LABEL)
label_words.grid(row=1, column=1, cnf=CNF_GRID)
label_word.grid(row=2, column=1, cnf=CNF_GRID)
entry.grid(row=3, column=1, cnf=CNF_GRID)
btn_start.grid(row=4, column=1, cnf=CNF_GRID)
label_time.grid(row=5, column=1, cnf=CNF_GRID)

root.mainloop()