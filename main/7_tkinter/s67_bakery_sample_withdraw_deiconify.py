from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

SIZE=128

BUTTON_CONFIG = {
    'activebackground': 'orange',
    'activeforeground': '#333333',
    'bg': '#333333',
    'fg': 'orange',
    'font': ('', 28),
    'padx': 5,
    'pady': 5,
}

def buy():
    if entry_pass.get()=='1111':
        messagebox.showinfo("Success", "Here you are.")
        exit()
    messagebox.showwarning("Warning!", "Your password is wrong")

def change_window():
    payment_window.deiconify()
    root.withdraw()

def add(label, amount):
    temp = int(label['text'])+amount
    if temp<0 or temp>20:
        temp = temp-amount
    label['text'] = temp

root = Tk()
root.geometry('1000x800+300+50')
root.config(bg='#333333')

label_sangak         = Label (root, text=0, cnf=BUTTON_CONFIG)
label_barbari        = Label (root, text=0, cnf=BUTTON_CONFIG)
label_lavash         = Label (root, text=0, cnf=BUTTON_CONFIG)
label_naylon         = Label (root, text=0, cnf=BUTTON_CONFIG)
button_sangak_minus  = Button(root, text='-', cnf=BUTTON_CONFIG, command=lambda:add(label_sangak, -1))
button_sangak_plus   = Button(root, text='+', cnf=BUTTON_CONFIG, command=lambda:add(label_sangak, 1))
button_barbari_minus = Button(root, text='-', cnf=BUTTON_CONFIG, command=lambda:add(label_barbari, -1))
button_barbari_plus  = Button(root, text='+', cnf=BUTTON_CONFIG, command=lambda:add(label_barbari, 1))
button_lavash_minus  = Button(root, text='-', cnf=BUTTON_CONFIG, command=lambda:add(label_lavash, -1))
button_lavash_plus   = Button(root, text='+', cnf=BUTTON_CONFIG, command=lambda:add(label_lavash, 1))
button_naylon_minus  = Button(root, text='-', cnf=BUTTON_CONFIG, command=lambda:add(label_naylon, -1))
button_naylon_plus   = Button(root, text='+', cnf=BUTTON_CONFIG, command=lambda:add(label_naylon, 1))
button_pay           = Button(root, text='Pay', cnf=BUTTON_CONFIG, command=lambda: change_window())
img_sangak = Image.open('C:/Users/Mohammad/Desktop/Zabt Python/python codes/main/7_tkinter/bakery/sangak.png')
img_barbari = Image.open('C:/Users/Mohammad/Desktop/Zabt Python/python codes/main/7_tkinter/bakery/barbari.png')
img_lavash = Image.open('C:/Users/Mohammad/Desktop/Zabt Python/python codes/main/7_tkinter/bakery/lavash.png')
img_naylon = Image.open('C:/Users/Mohammad/Desktop/Zabt Python/python codes/main/7_tkinter/bakery/naylon.png')
img_sangak = img_sangak.resize((SIZE, SIZE))
img_barbari = img_barbari.resize((SIZE, SIZE))
img_lavash = img_lavash.resize((SIZE, SIZE))
img_naylon = img_naylon.resize((SIZE, SIZE))
img_sangak = ImageTk.PhotoImage(img_sangak)
img_barbari = ImageTk.PhotoImage(img_barbari)
img_lavash = ImageTk.PhotoImage(img_lavash)
img_naylon = ImageTk.PhotoImage(img_naylon)
button_sangak = Button(root, cnf=BUTTON_CONFIG, image=img_sangak, relief='flat')
button_barbari = Button(root, cnf=BUTTON_CONFIG, image=img_barbari, relief='flat')
button_lavash = Button(root, cnf=BUTTON_CONFIG, image=img_lavash, command=lambda:add(label_lavash, 5))
button_naylon = Button(root, cnf=BUTTON_CONFIG, image=img_naylon, relief='flat')

button_sangak       .place(x=200,           y=10*1+SIZE*0, width=SIZE, height=SIZE)
button_sangak_minus .place(x=10,            y=10*1+SIZE*0, width=180, height=SIZE)
button_sangak_plus  .place(x=200+SIZE+10,   y=10*1+SIZE*0, width=180, height=SIZE)
label_sangak        .place(x=400+SIZE+10,   y=10*1+SIZE*0, width=180, height=SIZE)
button_barbari      .place(x=200,           y=10*2+SIZE*1, width=SIZE, height=SIZE)
button_barbari_minus.place(x=10,            y=10*2+SIZE*1, width=180, height=SIZE)
button_barbari_plus .place(x=200+SIZE+10,   y=10*2+SIZE*1, width=180, height=SIZE)
label_barbari       .place(x=400+SIZE+10,   y=10*2+SIZE*1, width=180, height=SIZE)
button_lavash       .place(x=200,           y=10*3+SIZE*2, width=SIZE, height=SIZE)
button_lavash_minus .place(x=10,            y=10*3+SIZE*2, width=180, height=SIZE)
button_lavash_plus  .place(x=200+SIZE+10,   y=10*3+SIZE*2, width=180, height=SIZE)
label_lavash        .place(x=400+SIZE+10,   y=10*3+SIZE*2, width=180, height=SIZE)
button_naylon       .place(x=200,           y=10*4+SIZE*3, width=SIZE, height=SIZE)
button_naylon_minus .place(x=10,            y=10*4+SIZE*3, width=180, height=SIZE)
button_naylon_plus  .place(x=200+SIZE+10,   y=10*4+SIZE*3, width=180, height=SIZE)
label_naylon        .place(x=400+SIZE+10,   y=10*4+SIZE*3, width=180, height=SIZE)
button_pay          .place(x=10,            y=10*5+SIZE*4, width=180, height=SIZE)


payment_window = Toplevel(root)
payment_window.protocol("WM_DELETE_WINDOW", root.destroy)
payment_window.withdraw()
payment_window.geometry("400x250+500+300")
entry_card = Entry(payment_window,   font=('', 48))
entry_pass = Entry(payment_window, show="*",   font=('', 48))
button_buy = Button(payment_window, text='Buy', command=buy,   font=('', 48))
entry_card.place(x=0, y=0, width=400, height=60)
entry_pass.place(x=0, y=65, width=300, height=60)
button_buy.place(x=0, y=130, width=250, height=100)
mainloop()