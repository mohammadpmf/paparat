from tkinter import *
from tkinter import messagebox, filedialog
import os

def save():
    name = entry_name.get().strip()
    surname = entry_surname.get()
    number = entry_number.get()
    result = filedialog.asksaveasfilename()
    if result in ["", None, ()]:
        messagebox.showerror("!", "File name can not be empty!")
        return
    with open(result, "w") as f:
        r = messagebox.askyesnocancel('Sure', 'Are your sure you want to save info?')
        if r==True:
            f.write(f'Name: {name}\nSurname: {surname}\nNumber: {number}')
        elif r==False:
            messagebox.showinfo("OK", "Ok. I wont save these info!")
        elif r==None:
            messagebox.showwarning("?", "I don't know what to do.")
    if r==False:
        os.remove(result)



root = Tk()
root.geometry('500x300+100+300')
root.title('صفحه اول')
# root2 = Toplevel(root)
# root2.geometry('400x300+600+300')
# root2.title('صفحه دوم')
# root3 = Toplevel(root)
# root3.geometry('400x300+1100+300')
# root3.title('😁')
label_name = Label(root, font=('', 14), text='Enter your name: ')
label_name.place(x=20, y=10, width=200, height=60)
entry_name = Entry(root, font=('', 14))
entry_name.place(x=240, y=10, width=240, height=60)
label_surname = Label(root, font=('', 14), text='Enter your surname: ')
label_surname.place(x=20, y=80, width=200, height=60)
entry_surname = Entry(root, font=('', 14))
entry_surname.place(x=240, y=80, width=240, height=60)
label_number = Label(root, font=('', 14), text='Enter your number: ')
label_number.place(x=20, y=150, width=200, height=60)
entry_number = Entry(root, font=('', 14))
entry_number.place(x=240, y=150, width=240, height=60)
button_save = Button(root, text="Save", font=('', 14), command=save)
button_save.place(x=50, y=220, width=140, height=60)
button_exit = Button(root, text="Exit", font=('', 14), command=exit)
button_exit.place(x=290, y=220, width=140, height=60)

root.mainloop()