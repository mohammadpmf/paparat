from tkinter import *
import pymysql


def set_password():
    query = "DELETE FROM `sql_injection_sample`.`users` WHERE;"
    cursor.execute(query)
    connection.commit()


connection = pymysql.connect(
    host="127.0.0.1", user="root", password="root", database="sql_injection_sample"
)
cursor = connection.cursor()

root = Tk()
label_username = Label(root, text="Username: ", font=("", 20))
label_password = Label(root, text="New Password: ", font=("", 20))
entry_username = Entry(root, font=("", 20))
entry_password = Entry(root, font=("", 20))
label_username.grid(row=1, column=1)
label_password.grid(row=2, column=1)
entry_username.grid(row=1, column=2)
entry_password.grid(row=2, column=2)
Button(root, text="Set New Passowrd", font=("", 20), command=set_password).grid(
    row=3, column=1, columnspan=2
)

root.mainloop()
