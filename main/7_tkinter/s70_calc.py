from tkinter import *

ENTRY_FONT = ('', 36)
REL_WIDTH = 0.137
REL_HEIGHT = 0.19
GAP = 0.005
CNF_BTN = {
    'bg': 'purple',
    'fg': 'orange',
    "font": ('', 24),
}

root = Tk()
root.config(bg='purple')
root.geometry('1000x500')
root.minsize(800, 400)
root.maxsize(1200, 600)
entry = Entry(root, font=ENTRY_FONT)
entry                                       .place(relx=REL_WIDTH*0+GAP*1, rely=REL_HEIGHT*0+GAP*1, relwidth=REL_WIDTH*6+GAP*5, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='copy')      .place(relx=REL_WIDTH*6+GAP*7, rely=REL_HEIGHT*0+GAP*1, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='|X|')       .place(relx=REL_WIDTH*0+GAP*1, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='1/X')       .place(relx=REL_WIDTH*1+GAP*2, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='√X')        .place(relx=REL_WIDTH*2+GAP*3, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='X²')        .place(relx=REL_WIDTH*3+GAP*4, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='2nd')       .place(relx=REL_WIDTH*4+GAP*5, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='*')         .place(relx=REL_WIDTH*5+GAP*6, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='←')         .place(relx=REL_WIDTH*6+GAP*7, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
for i in range(1, 6):
    Button(root, cnf=CNF_BTN, text=i)       .place(relx=REL_WIDTH*(i-1)+GAP*i, rely=REL_HEIGHT*2+GAP*3, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='/')         .place(relx=REL_WIDTH*5+GAP*6, rely=REL_HEIGHT*2+GAP*3, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='clear')     .place(relx=REL_WIDTH*6+GAP*7, rely=REL_HEIGHT*2+GAP*3, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
for i in range(6, 10):
    Button(root, cnf=CNF_BTN, text=i)       .place(relx=REL_WIDTH*(i-6)+GAP*(i-5), rely=REL_HEIGHT*3+GAP*4, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='0')         .place(relx=REL_WIDTH*4+GAP*5, rely=REL_HEIGHT*3+GAP*4, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='-')         .place(relx=REL_WIDTH*5+GAP*6, rely=REL_HEIGHT*3+GAP*4, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='+')         .place(relx=REL_WIDTH*6+GAP*7, rely=REL_HEIGHT*3+GAP*4, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*2+GAP*1)

Button(root, cnf=CNF_BTN, text='000')       .place(relx=REL_WIDTH*0+GAP*1, rely=REL_HEIGHT*4+GAP*5, relwidth=REL_WIDTH*2+GAP*1, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='.')         .place(relx=REL_WIDTH*2+GAP*3, rely=REL_HEIGHT*4+GAP*5, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='(')         .place(relx=REL_WIDTH*3+GAP*4, rely=REL_HEIGHT*4+GAP*5, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text=')')         .place(relx=REL_WIDTH*4+GAP*5, rely=REL_HEIGHT*4+GAP*5, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
Button(root, cnf=CNF_BTN, text='=', bg='green', fg='white', activebackground='lime', activeforeground='white')         .place(relx=REL_WIDTH*5+GAP*6, rely=REL_HEIGHT*4+GAP*5, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)


root.mainloop()