from tkinter import *
from random import choice, randint
ch = '0123456789abcdef'

root = Tk()
root.config(bg='#ffffff')
root.geometry('400x400+200+200')
lable_1 = Label(text='Salam', background='red', fg='orange', font=('consolas', 48))
lable_2 = Label(text='Khoobi?', bg='blue', font=('', 48))
lable_3 = Label(text='OK')
lable_4 = Label(text='Test', bg='yellow', foreground='green', font=("Calibri", 32, 'italic', 'bold', 'underline'))

lable_1.place(width=200, height=200, x=0, y=0)
lable_2.place(width=200, height=200, x=0, y=200)
lable_3.place(width=200, height=200, x=200, y=0)
lable_4.place(width=200, height=200, x=110, y=110)

# for i in range(10):
#     temp=Tk()
#     temp.config(bg=f"#{choice(ch)}{choice(ch)}{choice(ch)}{choice(ch)}{choice(ch)}{choice(ch)}")
#     temp.protocol("WM_DELETE_WINDOW", lambda :None)
#     temp.geometry(f"{randint(500, 1000)}x{randint(200, 700)}+{randint(100, 200)}+{randint(200, 700)}")

mainloop()