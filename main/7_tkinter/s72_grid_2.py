from tkinter import *

CNF_BTN={
    'bg':'#444555',
    'fg': 'orange',
    'bd': 12,
    'font': ('', 48)
}
CNF_GRID={
    'padx': 10,
    'pady': 10,
    'sticky': 'nesw',
}

root = Tk()
root.geometry('1000x800')

btn1  = Button(root, text=1, cnf=CNF_BTN)
btn2  = Button(root, text=2, cnf=CNF_BTN, anchor='nw', padx=20, pady=10, fg='green')
btn3  = Button(root, text=3, cnf=CNF_BTN, width=5)
btn4  = Button(root, text=4, cnf=CNF_BTN)
btn5  = Button(root, text=5, cnf=CNF_BTN)
btn6  = Button(root, text=6, cnf=CNF_BTN, width=5)
btn7  = Button(root, text=7, cnf=CNF_BTN)
btn8  = Button(root, text=8, cnf=CNF_BTN)
btn9  = Button(root, text=9, cnf=CNF_BTN)

btn1.grid(row=1, column=1, rowspan=1, columnspan=1, cnf=CNF_GRID)
btn2.grid(row=1, column=2, rowspan=2, columnspan=2, cnf=CNF_GRID)
btn3.grid(row=1, column=4, rowspan=1, columnspan=1, cnf=CNF_GRID)
btn4.grid(row=2, column=1, rowspan=1, columnspan=1, cnf=CNF_GRID)
btn5.grid(row=3, column=2, rowspan=1, columnspan=1, cnf=CNF_GRID)
btn6.grid(row=2, column=4, rowspan=2, columnspan=1, cnf=CNF_GRID)
btn7.grid(row=4, column=1, rowspan=1, columnspan=4, cnf=CNF_GRID)
btn8.grid(row=3, column=1, rowspan=1, columnspan=1, cnf=CNF_GRID)
btn9.grid(row=3, column=3, rowspan=1, columnspan=1, cnf=CNF_GRID)

root.mainloop()