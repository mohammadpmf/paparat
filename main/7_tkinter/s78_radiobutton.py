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

root = Tk()
root.geometry('1000x600')
root.config(bg='#333333')
Label(root, CNF, text='Origin:').grid(row=1, column=1, columnspan=10, cnf=CNF_GRID)
Label(root, CNF, text='Destination:').grid(row=3, column=1, columnspan=10, cnf=CNF_GRID) 
Button(root, CNF, text='Buy', width=16).grid(row=5, column=1, columnspan=2, cnf=CNF_GRID)
root.mainloop()