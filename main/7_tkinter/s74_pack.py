from tkinter import *

root = Tk()
root.geometry('600x600+300+400')
frame_top       = Frame(root, bg='green')
frame_bottom    = Frame(root, bg='white')
label_name      = Label(frame_top, anchor='ne', padx=60, pady=40, text='Enter your name: ', bg='pink', font=('', 26))
label_number    = Label(frame_top, text='Enter your number: ', bg='tomato', font=('', 26))
entry_name      = Entry(frame_bottom, bg='#555555', font=('', 26))
entry_number    = Entry(frame_bottom, bg='sky blue', font=('', 26))

frame_top.pack(fill='both', expand=1)
frame_bottom.pack(fill='both', expand=1)
label_name.pack(side='left', expand=1, fill='both', padx=20, pady=20, ipadx=150)
# https://stackoverflow.com/questions/67866115/is-ipad-x-y-and-pad-x-y-different-in-tkinter-python
label_number.pack(side='left', expand=1)
entry_name.grid(row=1, column=1)
entry_number.grid(row=2, column=2)


root.mainloop()