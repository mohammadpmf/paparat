from tkinter import *
import random
import string
import pyperclip
from tkinter import filedialog

BG='skyblue',
FG='purple'

CNF_CHECKBUTTON = {
    'bg': BG,
    'fg': FG,
    'font': ('', 24)
}

CNF_LABEL = {
    'bg': BG,
    'fg': FG,
    'font': ('', 24)
}

CNF_BTN = {
    'bg': BG,
    'fg': FG,
    'font': ('', 24)
}

CNF_ENTRY = {
    'bg': BG,
    'fg': FG,
    'font': ('', 32),
    'width': 30,
    'justify': 'center',
}

CNF_SPIN = {
    'bg': BG,
    'fg': FG,
    'width': 3,
    'justify': 'center',
    'font': ('', 24),
    'disabledbackground':'dark gray',
    'disabledforeground':'gray',
    'wrap': False
}

CNF_GRID = {
    'padx': 10,
    'pady': 5,
    'sticky': 'w'
}

def generate():
    if bv_default_length.get()==False:
        min_length = int(spin_min.get())
        max_length = int(spin_max.get())
    else:
        min_length=12
        max_length=16
    length = random.randint(min_length, max_length)
    characters = ''
    if bv_lower.get():
        characters += string.ascii_lowercase
    if bv_upper.get():
        characters += string.ascii_uppercase
    if bv_number.get():
        characters += string.digits
    temp = []
    if bv_punctuation.get():
        for i in range (int(spin_punctuation_number.get())):
            temp.append(random.choice(string.punctuation))
        length = length-int(spin_punctuation_number.get())
    if characters=='':
        characters = string.ascii_lowercase
        bv_lower.set(True)
    for _ in range(length):
        char = random.choice(characters)
        temp.append(char)
    random.shuffle(temp)
    temp = ''.join(temp)
    return temp

def check():
    if bv_default_length.get():
        spin_min.config(state='disabled')
        spin_max.config(state='disabled')
    else:
        spin_min.config(state='readonly')
        spin_max.config(state='readonly')
    if bv_punctuation.get():
        frame.grid(row=2, column=4, cnf=CNF_GRID)
    else:
        frame.grid_forget()

        
def generate_password():
    global result
    result = generate()
    pyperclip.copy(result)
    entry.delete(0, END)
    entry.insert(0, result)

def save():
    global result
    name = filedialog.asksaveasfilename()
    with open(name, 'w') as f:
        # f.write(pyperclip.paste())
        f.write(result)

root = Tk()
root.config(bg=BG)
root.resizable(False, False)
bv_lower = BooleanVar(root)
bv_upper = BooleanVar(root)
bv_number = BooleanVar(root)
bv_punctuation = BooleanVar(root)
bv_default_length = BooleanVar(root)
bv_default_length.set(True)
Checkbutton(root, variable=bv_lower, text='use lower case', cnf=CNF_CHECKBUTTON).grid(row=1, column=1, cnf=CNF_GRID)
Checkbutton(root, variable=bv_upper, text='use upper case', cnf=CNF_CHECKBUTTON).grid(row=1, column=2, cnf=CNF_GRID)
Checkbutton(root, variable=bv_number, text='use numbers', cnf=CNF_CHECKBUTTON).grid(row=1, column=3, cnf=CNF_GRID)
Checkbutton(root, variable=bv_punctuation, text='use punctuations', cnf=CNF_CHECKBUTTON, command=check).grid(row=1, column=4, cnf=CNF_GRID)
Checkbutton(root, variable=bv_default_length, text='use defalut length (12, 16)', cnf=CNF_CHECKBUTTON, command=check).grid(row=2, column=1, columnspan=2, cnf=CNF_GRID)
Label(root, text='Minimum Length: ', cnf=CNF_LABEL).grid(row=3, column=1, cnf=CNF_GRID)
Label(root, text='Maximum Length: ', cnf=CNF_LABEL).grid(row=4, column=1, cnf=CNF_GRID)
spin_min = Spinbox(root, from_=4, to=8, cnf=CNF_SPIN, state='disabled')
spin_max = Spinbox(root, from_=8, to=20, cnf=CNF_SPIN, state='disabled')
frame = Frame(root, bg=BG)
Label(frame, text='Number: ', cnf=CNF_LABEL).grid(row=1, column=1, cnf=CNF_GRID)
spin_punctuation_number = Spinbox(frame, from_=1, to=6, cnf=CNF_SPIN, state='readonly')
spin_min.grid(row=3, column=2, cnf=CNF_GRID)
spin_max.grid(row=4, column=2, cnf=CNF_GRID)
spin_punctuation_number.grid(row=1, column=2, cnf=CNF_GRID)
Button(root, text='Generate Password', cnf=CNF_BTN, command=generate_password).grid(row=5, column=1, cnf=CNF_GRID)
Button(root, text='Save this Password', cnf=CNF_BTN, command=save).grid(row=6, column=1, cnf=CNF_GRID)
entry = Entry(root, cnf=CNF_ENTRY)
entry.grid(row=5, column=2, columnspan=3, cnf=CNF_GRID)
root.mainloop()

# lower
# upper
# punctuation
# numbers
# default length => 16 enable and disable => spinbox
# spinbox is disabled at first => range 12 - 16
# save by dialog to where and wich name