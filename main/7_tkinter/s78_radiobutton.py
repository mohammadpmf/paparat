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
def show():
    print(sv_origin.get())
    print(sv_destination.get())
    
root = Tk()
root.geometry('1000x600')
root.config(bg='#333333')
Label(root, CNF, text='Origin:').grid(row=1, column=1, columnspan=10, cnf=CNF_GRID)
sv_origin = StringVar(root)
sv_origin.set('')
Radiobutton(root, CNF, variable=sv_origin, value='Tehran', text='Tehran').grid(row=2, column=1, cnf=CNF_GRID)
Radiobutton(root, CNF, variable=sv_origin, value='Rasht', text='Rasht').grid(row=2, column=2, cnf=CNF_GRID)
Radiobutton(root, CNF, variable=sv_origin, value='Isfahan', text='Isfahan').grid(row=2, column=3, cnf=CNF_GRID)
Radiobutton(root, CNF, variable=sv_origin, value='Mashhad', text='Mashhad').grid(row=2, column=4, cnf=CNF_GRID)
sv_destination = StringVar(root)
sv_destination.set('')
Label(root, CNF, text='Destination:').grid(row=3, column=1, columnspan=10, cnf=CNF_GRID) 
Radiobutton(root, CNF, variable=sv_destination, value='Tehran', text='Tehran').grid(row=4, column=1, cnf=CNF_GRID)
Radiobutton(root, CNF, variable=sv_destination, value='Rasht', text='Rasht').grid(row=4, column=2, cnf=CNF_GRID)
Radiobutton(root, CNF, variable=sv_destination, value='Isfahan', text='Isfahan').grid(row=4, column=3, cnf=CNF_GRID)
Button(root, CNF, text='Buy', width=16, command=show).grid(row=5, column=1, columnspan=2, cnf=CNF_GRID)
root.mainloop()