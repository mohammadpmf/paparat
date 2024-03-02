from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# img = PhotoImage(master=root, file='C:/Users/Mohammad/Desktop/Zabt Python/python codes/main/7_tkinter/bakery/barbari.jpg')
img = Image.open('C:/Users/Mohammad/Desktop/Zabt Python/python codes/main/7_tkinter/bakery/barbari.png')
img = img.resize((200, 200))
img = ImageTk.PhotoImage(img)
label_pic = Label(root, image=img)
label_pic.place(x=0, y=0, width=200, height=200)

mainloop()