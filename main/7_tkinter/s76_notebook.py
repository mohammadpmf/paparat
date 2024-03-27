from tkinter import *
from tkinter import ttk

CNF_BTN = {
    'font': ('', 24),
    'padx': 10,
    'pady': 5,
}
CNF_LBL = {
    'font': ('', 24),
    'padx': 10,
    'pady': 5,
}
CNF_ENTRY = {
    'font': ('', 24),
}
CNF_GRID = {
    'padx': 20,
    'pady': 10,
}

def c2f(celecius):
    return round(celecius*1.8+32, 1)

def f2c(fahrenheit):
    return round((fahrenheit-32)/1.8, 1)

def bmi(height, mass):
    return round(mass/(height**2), 1)

def print_bmi():
    try:
        mass = float(entry_mass.get())
        height = float(entry_height.get())/100
        result = bmi(height, mass)
        label_bmi.config(text=result)
    except:
        label_bmi.config(text='Error')

def print_c2f():
    try:
        c = float(entry_c.get())
        f = c2f(c)
        label_f.config(text=f)
    except:
        label_f.config(text='Error')

def print_f2c():
    try:
        f = float(entry_f.get())
        c = f2c(f)
        label_c.config(text=c)
    except:
        label_c.config(text='Error')

root = Tk()
# root.geometry('800x600')
tabs = ttk.Notebook(root)
tab_c2f = ttk.Frame(tabs)
tab_f2c = ttk.Frame(tabs)
tab_bmi = ttk.Frame(tabs)
tabs.add(tab_c2f, text ='تبدیل سلسیوس به فارنهایت')
tabs.add(tab_f2c, text ='تدبیل فارنهایت به سلسیوس')
tabs.add(tab_bmi, text ='محاسبه شاخص توده بدنی')


entry_c = Entry(tab_c2f, cnf=CNF_ENTRY)
entry_f = Entry(tab_f2c, cnf=CNF_ENTRY)
entry_mass = Entry(tab_bmi, cnf=CNF_ENTRY)
entry_height = Entry(tab_bmi, cnf=CNF_ENTRY)

entry_c.grid(row=1, column=1, cnf=CNF_GRID)
entry_f.grid(row=1, column=1, cnf=CNF_GRID)

btn_c2f = Button(tab_c2f, cnf=CNF_BTN, text='محاسبه کن', command=print_c2f).grid(row=2, column=1, cnf=CNF_GRID)
btn_f2c = Button(tab_f2c, cnf=CNF_BTN, text='محاسبه کن', command=print_f2c).grid(row=2, column=1, cnf=CNF_GRID)
btn_bmi = Button(tab_bmi, cnf=CNF_BTN, text='محاسبه کن', command=print_bmi).grid(row=3, column=2, cnf=CNF_GRID)

Label(tab_bmi, cnf=CNF_LBL, text="وزن خود را به کیلوگرم وارد کنید").grid(row=1, column=2, cnf=CNF_GRID)
Label(tab_bmi, cnf=CNF_LBL, text="قد خود را به سانتیمتر وارد کنید").grid(row=2, column=2, cnf=CNF_GRID)
label_bmi = Label(tab_bmi, cnf=CNF_LBL, text='')
label_c = Label(tab_f2c, cnf=CNF_LBL, text='')
label_f = Label(tab_c2f, cnf=CNF_LBL, text='')

label_c.grid(row=3, column=1, cnf=CNF_GRID)
label_f.grid(row=3, column=1, cnf=CNF_GRID)


label_bmi.grid(row=3, column=1, cnf=CNF_GRID)
entry_mass.grid(row=1, column=1, cnf=CNF_GRID)
entry_height.grid(row=2, column=1, cnf=CNF_GRID)

tabs.pack(expand = 1, fill ="both")
root.mainloop()