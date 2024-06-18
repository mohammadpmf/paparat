from tkinter import *
from tkinter import messagebox
from random import randint
from time import sleep
from threading import Thread

CORRECT_COLOR = 'green'
WRONG_COLOR = 'pink'
SLEEP_TIME = 0
time = 0
number_of_moves = 0
is_playing = False
record = "59:59"
is_moving = False
houses = [
    (0, 0), (0, 1), (0, 2), (0, 3),
    (1, 0), (1, 1), (1, 2), (1, 3),
    (2, 0), (2, 1), (2, 2), (2, 3),
    (3, 0), (3, 1), (3, 2), (3, 3),
]


class Square():
    def __init__(self, root, text=None, width=6, height=3):
        self.root = root
        self.is_in_right_place = False
        self.left = False
        self.right = False
        self.top = False
        self.bottom = False
        self.can_move = False
        self.text = text
        self.width = width
        self.height = height
        self.btn = Button(self.root, font=('', 20), text=self.text, width=self.width, height=self.height, command=self.check_and_move)
    
    def place(self, *args, **kwargs):
        self.btn.place(*args, **kwargs)
        
    def check_and_move(self):
        if self.can_move:
            self.move()
        else:
            messagebox.showerror("Invalid move!", "Can't move this Square!!!")
    
    def move(self):
        global empty, is_moving, is_playing, number_of_moves
        is_moving = True
        disable_all()
        info = self.btn.place_info()
        x = int((float(info['relx']))*4)
        y = int((float(info['rely']))*4)
        if self.left:
            i = x/4
            while i>x/4-0.26:
                self.btn.place(relx=i)
                sleep(SLEEP_TIME)
                i-=0.01
                root.update()
        elif self.right:
            i = x/4
            while i<x/4+0.26:
                self.btn.place(relx=i)
                sleep(SLEEP_TIME)
                i+=0.01
                root.update()
        elif self.top:
            i = y/4
            while i>y/4-0.26:
                self.btn.place(rely=i)
                sleep(SLEEP_TIME)
                i-=0.01
                root.update()
        elif self.bottom:
            i = y/4
            while i<y/4+0.26:
                self.btn.place(rely=i)
                sleep(SLEEP_TIME)
                i+=0.01
                root.update()
        empty = x, y
        number_of_moves+=1
        enable_all()
        is_moving = False
        set_states()
        if is_finished():
            is_playing = False
            if messagebox.askyesno("Congratulations", "Yey:D\nYou have solved the puzzle.\nWant to Save your record?"):
                save_record()
            if messagebox.askyesno("Play again?", "Want to play again?"):
                restart()
            else:
                messagebox.showinfo(":)", "Ok.\nGood Luck!")
                exit()
    def move_to_shuffle(self):
        global empty
        info = self.btn.place_info()
        x = int((float(info['relx']))*4)
        y = int((float(info['rely']))*4)
        if self.left:
            self.btn.place(relx=x/4-0.25)
        elif self.right:
            self.btn.place(relx=x/4+0.25)
        elif self.top:
            self.btn.place(rely=y/4-0.25)
        elif self.bottom:
            self.btn.place(rely=y/4+0.25)
        empty = x, y
        set_states()


def save_record():
    global record, number_of_moves
    n = 1
    try:
        f = open('records.txt', 'r')
        n = len(f.readlines())+1
        f.close()
    except FileNotFoundError:
        pass
    f = open('records.txt', 'a')
    f.write(f"Record number {n}: {record}s\tNumber of moves: {number_of_moves} times.\n")
    f.close()


def count_time():
    global is_playing, time, record
    while is_playing:
        time+=1
        sleep(1)
        root.title(f"{time//60:02}:{time%60:02}")
    record = f"{time//60:02}:{time%60:02}"
    print(record)


def shuffle():
    global is_playing
    is_playing = False
    for i in range(randint(100, 140)):
        for square in squares:
            square: Square
            if square.can_move:
                if randint(0, 1):
                    square.move_to_shuffle()
    root.update()
    is_playing = True


def is_finished():
    for square in squares:
        square: Square
        if square.is_in_right_place == False:
            return False
    return True


def enable_all():
    for square in squares:
        square: Square
        square.btn.config(state='normal')


def disable_all():
    for square in squares:
        square: Square
        square.btn.config(state='disabled')


def set_movement_state():
    for square in squares:
        square: Square
        if square.left == True or square.right == True or square.top == True or square.bottom == True:
            square.can_move=True
        else:
            square.can_move=False


def set_right_place_state():
    for square in squares:
        square: Square
        number = int(square.btn['text'])
        info = square.btn.place_info()
        x = int((float(info['relx']))*4)
        y = int((float(info['rely']))*4)
        if number == x+4*y+1:
            square.is_in_right_place = True
            square.btn.config(bg=CORRECT_COLOR)
        else:
            square.is_in_right_place = False
            square.btn.config(bg=WRONG_COLOR)


def set_states():
    global empty
    for square in squares:
        square: Square
        info = square.btn.place_info()
        x = int((float(info['relx']))*4)
        y = int((float(info['rely']))*4)
        if abs(x-empty[0])==1 and abs(y-empty[1])==0:
            if x-empty[0]==1:
                square.left=True
                square.right=False
            else:
                square.left=False
                square.right=True
            square.top=False
            square.bottom=False
        elif abs(y-empty[1])==1 and abs(x-empty[0])==0:
            if y-empty[1]==1:
                square.top=True
                square.bottom=False
            else:
                square.top=False
                square.bottom=True
            square.left=False
            square.right=False
        else:
            square.top=False
            square.bottom=False
            square.left=False
            square.right=False
    set_movement_state()
    set_right_place_state()


def reset():
    global empty, number_of_moves, time
    time = 0
    number_of_moves = 0
    temp = houses.copy()
    for i in range(15):
        house = temp.pop(0)
        x, y = house
        squares[i].place(relx=x/4, rely=y/4, relwidth=0.25, relheight=0.25)
    empty = temp.pop()
    set_states()
    shuffle()


def restart():
    reset()
    Thread(target=count_time, daemon=True).start()


def key_release(event:Event):
    global is_moving
    if event.keysym=='r':
        reset()
        return
    if event.keysym=='a':
        is_moving=False
        return
    if not is_moving:
        is_moving = True
        if event.keysym == "Left":
            for square in squares:
                square: Square
                if square.left:
                    square.move()
                    is_moving = False
                    return
        elif event.keysym == "Right":
            for square in squares:
                square: Square
                if square.right:
                    square.move()
                    is_moving = False    
                    return
        elif event.keysym == "Up":
            for square in squares:
                square: Square
                if square.top:
                    square.move()
                    is_moving = False    
                    return
        elif event.keysym == "Down":
            for square in squares:
                square: Square
                if square.bottom:
                    square.move()
                    is_moving = False    
                    return
        else:
            is_moving = False


messagebox.showinfo("Description", "Welcome.\nYou Should put numbers in order from 1 to 15.\nWhen each number is in the right place, it changes to green.\nWhen all numbers are in their places puzzle is finished.\nYou can click on buttons to move them or use arrow keys on keyboard.\nIf arrow keys stuck, press 'a' on keyboard.\nPress r to reset the game.")
root = Tk()
# root.iconbitmap(r'1.ico')
root.focus_force()
root.bind('<KeyRelease>', key_release)
root.geometry('800x800')
squares = []
for i in range(1, 16):
    squares.append(Square(root, text=i))
restart()

root.mainloop()