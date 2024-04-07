from tkinter import *
from tkinter import messagebox as msb
from threading import Thread
from random import random, randint
from time import sleep

SIZE = 3
SIZE2 = SIZE**2
PLAYING_TIME = 3
BG='#444444'
TARGET_COLOR = 'red'

CNF_BNT = {
    'font': ('', 28),
    'bd': 12,
    'bg': BG,
    'width': 5,
    'height': 3,
    'activebackground': 'light green'
}

CNF_GRID = {
    'padx':1,
    'pady':1,
}

def bonus():
    temp = randint(0, SIZE2-1)
    btns[temp].config(bg=TARGET_COLOR)
    t = random()*0.4+0.6
    sleep(t)
    btns[temp].config(bg=BG)

def start_game():
    global score, right_clicks, wrong_clicks
    time = PLAYING_TIME
    while time>0:
        temp = randint(0, SIZE2-1)
        btns[temp].config(bg=TARGET_COLOR)
        t = random()*0.4+0.6
        sleep(t)
        time -= t
        btns[temp].config(bg=BG)
    message = f"Your score is: {score}\nRight Clicks: {right_clicks}\nWrong Clicks: {wrong_clicks}\nAccuracy: {round(right_clicks*100/(right_clicks+wrong_clicks),2)}%"
    msb.showinfo("Game Finished", message)
    root.destroy()

def start():
    btn_start.grid_forget()
    Thread(target=start_game, daemon=True).start()

def check(n):
    global score, right_clicks, wrong_clicks
    if btns[n]['bg']==TARGET_COLOR:
        score += 3
        right_clicks += 1
        btns[n].config(bg=BG)
        Thread(target=bonus, daemon=True).start()
    else:
        score -= 1
        wrong_clicks += 1

score = 0
right_clicks = 0
wrong_clicks = 0
root = Tk()
root.geometry('+1250+200')
root.config(bg=BG)
btns = []
for i in range(SIZE2):
    btns.append(Button(root, cnf=CNF_BNT, command=lambda i=i:check(i)))
for i in range(SIZE):
    for j in range(SIZE):
        btns[i*SIZE+j].grid(row=i, column=j, cnf=CNF_GRID)
btn_start = Button(root, cnf=CNF_BNT, text='start', command=start)
btn_start.grid(row=SIZE, column=0, columnspan=SIZE, sticky='news', cnf=CNF_GRID)

root.mainloop()