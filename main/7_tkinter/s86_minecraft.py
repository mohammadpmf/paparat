from tkinter import *
from tkinter import colorchooser


class MineCraftCharacter:
    def __init__(self, root: Tk):
        self.root = root
        self.frame = Frame(self.root, bg='pink')
        self.root.bind_all('<Key>', self.action)
        self.eye1  = Label(self.frame, bg='black')
        self.eye2  = Label(self.frame, bg='black')
        self.nose  = Label(self.frame, bg='red')
        self.mouse = Label(self.frame, bg='sky blue')
        self.hair  = Label(self.frame, bg='purple')
        self.btn_face_color  = Button(self.root, text='face', command=lambda: self.select_color(self.frame))
        self.btn_eye_color   = Button(self.root, text='eyes', command=lambda: self.select_color(self.eye1))
        self.btn_nose_color  = Button(self.root, text='nose', command=lambda: self.select_color(self.nose))
        self.btn_mouse_color = Button(self.root, text='mosue', command=lambda: self.select_color(self.mouse))
        self.btn_hair_color  = Button(self.root, text='hair', command=lambda: self.select_color(self.hair))
        self.eye1.place(x=40, y=55, width=25, height=25)
        self.eye2.place(x=120, y=55, width=25, height=25)
        self.nose.place(x=80, y=100, width=25, height=25)
        self.mouse.place(x=40, y=145, width=110, height=20)
        self.hair.place(x=0, y=0, width=200, height=30)
        self.btn_face_color.grid(row=1, column=1)
        self.btn_eye_color.grid(row=1, column=2)
        self.btn_nose_color.grid(row=1, column=3)
        self.btn_mouse_color.grid(row=1, column=4)
        self.btn_hair_color.grid(row=1, column=5)

    def select_color(self, item: Label):
        answer = colorchooser.askcolor()[1]
        if item==self.eye1:
            self.eye2.config(bg=answer)
        item.config(bg=answer)

    def action(self, event):
        btn = event.keysym
        movement_speed = 10
        if btn=='Right':
            x = int(self.frame.place_info().get('x'))
            x += movement_speed
            self.frame.place(x=x)
        elif btn=='Left':
            x = int(self.frame.place_info().get('x'))
            x -= movement_speed
            self.frame.place(x=x)
        elif btn=='Up':
            y = int(self.frame.place_info().get('y'))
            y -= movement_speed
            self.frame.place(y=y)
        elif btn=='Down':
            y = int(self.frame.place_info().get('y'))
            y += movement_speed
            self.frame.place(y=y)

    def place(self, x=0, y=0):
        self.frame.place(x=x, y=y, width=200, height=200)


root = Tk()
root.geometry('1000x800')
character1 = MineCraftCharacter(root)
character1.place(x=100, y=50)

mainloop()