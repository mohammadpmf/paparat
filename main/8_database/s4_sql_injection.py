from tkinter import *
from tkinter import messagebox as msb
import pymysql

def login():
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    query = f"SELECT * FROM new_table WHERE username='{username}' AND password='{password}';"
    cursor.execute(query)
    # query = "SELECT * FROM new_table WHERE username=%s AND password=%s;"
    # values = username, password
    # cursor.execute(query, values)
    result = cursor.fetchone()
    if result:
        msb.showinfo("Welcome", f"Welcome {result[1]} with ID {result[0]} in Database!")
    else:
        msb.showerror("Error", f"wrong username or password!")


connection = pymysql.connect(host='127.0.0.1', user='root', password='root', database="sql_injection_sample")
cursor = connection.cursor()

root = Tk()
label_username = Label(root, text='Username: ', font=("", 20))
label_password = Label(root, text='Password: ', font=("", 20))
entry_username = Entry(root, font=("", 20))
entry_password = Entry(root, font=("", 20))
label_username.grid(row=1, column=1)
label_password.grid(row=2, column=1)
entry_username.grid(row=1, column=2)
entry_password.grid(row=2, column=2)
Button(root, text="Login", font=("", 20), command=login).grid(row=3, column=1, columnspan=2)

root.mainloop()