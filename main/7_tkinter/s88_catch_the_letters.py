from tkinter import *
from string import ascii_letters
from threading import Thread
from time import sleep
from tkinter import messagebox
import random


COLORS = ['red', 'green', 'blue', 'lime', 'yellow', 'brown', 'purple', 'tomato', 'orange', 'cyan', 'dark cyan',
          'sky blue', 'gray', 'gold', 'silver', 'violet', 'magenta', '#149361', 'pink', 'dark green',
          'light green', '#991146']


def start():
    while len(letters)!=0:
        letter = random.choice(letters)
        letters.remove(letter)
        Thread(target=go_down, args=(letter, ), daemon=True).start()
        sleep(random.uniform(0.2, 0.8))
    sleep(3)
    messagebox.showinfo("Score", f"Your score is {len(me['text'])}")


def go_down(letter: str):
    b = Button(root, text=letter, bg=random.choice(COLORS))
    x=random.randint(0, 270)
    for i in range(0, 601, 10):
        if i>510:
            if x>p-30 and x<p+100:
                me['text'] += letter
                b.place_forget()
                return
            else:
                b.place(x=x, y=i, width=30, height=50)
        else:
            b.place(x=x, y=i, width=30, height=50)
        sleep(0.05)


def key_press(e: Event):
    global p
    if e.keysym == 'Right' and p<200:
        p+=5
        me.place(x=p)
    elif e.keysym == 'Left' and p>0:
        p-=5
        me.place(x=p)


letters = list(ascii_letters)
p=100
root = Tk()
root.bind("<KeyPress>", key_press)
root.geometry("300x600+300+150")
root.config(bg="#222222")
me = Button(root, bg='white', font=('', 6), wraplength=100)
me.place(x=100,y=550, width=100, height=50)
Thread(target=start, daemon=True).start()
root.mainloop()
