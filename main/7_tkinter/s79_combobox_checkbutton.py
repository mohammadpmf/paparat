from tkinter import *
from tkinter import ttk

CNF={
    'font': ('', 22),
    'bg': 'sky blue',
    'fg': 'purple',
}
CNF_GRID = {
    'padx': 10,
    'pady': 20,
}
foods = ['Fish', 'Kebab', 'Pizza', 'Pasta','Fish', 'Kebab', 'Pizza', 'Pasta','Fish', 'Kebab', 'Pizza', 'Pasta','Fish', 'Kebab', 'Pizza', 'Pasta','Fish', 'Kebab', 'Pizza', 'Pasta','Fish', 'Kebab', 'Pizza', 'Pasta','Fish', 'Kebab', 'Pizza', 'Pasta','Fish', 'Kebab', 'Pizza', 'Pasta','Fish', 'Kebab', 'Pizza', 'Pasta']

def show():
    print(bv_salad.get())
    
root = Tk()
root.geometry('1000x600')
root.config(bg='sky blue')
Label(root, CNF, text='Main dish:').grid(row=1, column=1, cnf=CNF_GRID)
combobox = ttk.Combobox(root, values=foods, state='readonly')
combobox.grid(row=1, column=2, cnf=CNF_GRID)
bv_salad = BooleanVar(root)
Checkbutton(root, CNF, text='salad', variable=bv_salad).grid(row=2, column=1, sticky='w')
Checkbutton(root, CNF, text='coca cola').grid(row=3, column=1, sticky='w')
Checkbutton(root, CNF, text='water').grid(row=4, column=1, sticky='w')
Checkbutton(root, CNF, text='mast').grid(row=5, column=1, sticky='w')
Button(root, CNF, text='Order', width=16, command=show).grid(row=6, column=1, cnf=CNF_GRID)
root.mainloop()