from tkinter import *

CNF={
    'font': ('', 24),
    'bg': '#333333',
    'fg': 'orange',
}
CNF_GRID = {
    'padx': 10,
    'pady': 20,
}

def change_color():
    s1.set(e1.get())
    

root = Tk()
root.config(bg='#333333')

s1 = StringVar(root)
e1 = StringVar(root)
e2 = StringVar(root)
Label(root, CNF, textvariable=s1).grid(row=1, column=1, cnf=CNF_GRID)
Label(root, CNF, text="Enter your age: ").grid(row=2, column=1, cnf=CNF_GRID)
Entry(root, CNF, textvariable=e1).grid(row=1, column=2, cnf=CNF_GRID)
Entry(root, CNF, textvariable=e2).grid(row=2, column=2, cnf=CNF_GRID)
Button(root, CNF, text='OK', textvariable=e1, command=change_color).grid(row=3, column=1, columnspan=2, sticky='news', cnf=CNF_GRID, padx=120)
root.mainloop()