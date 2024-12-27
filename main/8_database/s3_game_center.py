from tkinter import *
from tkinter import messagebox as msb
from config import *
from connection import Connection


def change_window(hide_window: Tk, show_window: Tk):
    global access_level
    hide_window.withdraw()
    show_window.deiconify()
    if show_window==main_window:
        if access_level==1:
            btn_view_orders_main_window_manager      .grid(row=1, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)
            btn_view_orders_main_window_user         .grid_forget()
            btn_add_update_delete_game_main_window   .grid(row=2, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)
        else:
            btn_view_orders_main_window_manager      .grid_forget()
            btn_view_orders_main_window_user         .grid(row=1, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)
            btn_add_update_delete_game_main_window   .grid_forget()


def create_account():
    name = entry_name_sign_up_window.get().strip()
    surname = entry_surname_sign_up_window.get().strip()
    username = entry_username_sign_up_window.get().strip()
    password1 = entry_password1_sign_up_window.get().strip()
    password2 = entry_password2_sign_up_window.get().strip()
    if username == "":
        msb.showerror("Username Error", "Username can not be empty!")
        return
    if password1 != password2:
        msb.showerror("Password Error", "Passwords do not match!")
        return
    if len(password1)<4:
        msb.showerror("Password Error", "Password must be at least 4 characters!")
        return
    if name=='': name=None
    if surname=='': surname=None
    result = connection.insert_user(username, password1, name, surname)
    if result[1] == "OK":
        entry_name_sign_up_window.delete(0, END)
        entry_surname_sign_up_window.delete(0, END)
        entry_username_sign_up_window.delete(0, END)
        entry_password1_sign_up_window.delete(0, END)
        entry_password2_sign_up_window.delete(0, END)
        change_window(sign_up_window, root)
        msb.showinfo("Success", f"Account {username} created successfully!")
    elif result[1] == "Duplicate":
        msb.showerror("Error", f"Account {username} already exists!")
        entry_username_sign_up_window.focus_set()


def login():
    global access_level
    username = entry_username_login_window.get().strip()
    password = entry_password_login_window.get().strip()
    if username == '':
        msb.showerror("Username Error", "Username can not be empty!")
        return
    if len(password) < 4:
        msb.showerror("Password Error", "Password must be at least 4 characters!")
        return
    result = connection.login(username, password)
    message = result[1]
    if result[0]==-1:
        msb.showerror("Error", message)
    elif result[0]==0:
        access_level = result[2]
        change_window(login_window, main_window)
        msb.showinfo("Successfull Login", message)


def create_game():
    name = entry_name_add_update_delete_window.get().strip()
    company = entry_company_add_update_delete_window.get().strip()
    date = entry_date_add_update_delete_window.get().strip()
    price = entry_price_add_update_delete_window.get().strip()
    genre = entry_genre_add_update_delete_window.get().strip()
    age_range = entry_age_range_add_update_delete_window.get().strip()
    if name == "":
        msb.showerror("Name Error", "You must enter a name for game!")
        entry_name_add_update_delete_window.focus_set()
        return
    if company == "":
        msb.showerror("Company Error", "You must enter a name for company!")
        entry_company_add_update_delete_window.focus_set()
        return
    if date == "":
        msb.showerror("Company Error", "You must enter a date!")
        entry_date_add_update_delete_window.focus_set()
        return
    if price == "":
        msb.showerror("Company Error", "You must enter game's price!")
        entry_price_add_update_delete_window.focus_set()
        return
    if genre == "":
        msb.showerror("Company Error", "You must enter game's genre!")
        entry_genre_add_update_delete_window.focus_set()
        return
    if age_range == "":
        msb.showerror("Company Error", "You must enter game's age_range!")
        entry_age_range_add_update_delete_window.focus_set()
        return
    date = f"{date}-01-01"
    result = connection.insert_game(name, company, date, price, genre, age_range)
    if result[1] == "OK":
        message = f"Game {name} created successfully."
        msb.showinfo("Success", message)
    elif result[1] == "Duplicate":
        message = f"Game {name} already exists!"
        msb.showerror("Error", message)
    elif result[1] == "Age":
        message = f"Age must be between 0 and 255"
        msb.showerror("Error", message)
    elif result[1] == "Price":
        message = f"Price must be between 00.00 and 99.99"
        msb.showerror("Error", message)
    elif result[1] == "Long Data":
        message = f"Too long data for one field"
        msb.showerror("Error", message)
    elif result[1] == "Unknown Error":
        msb.showerror("Error", result[1])
        
    

connection = Connection()
if not connection.check_connection():
    msb.showerror("Error", "Could not connect to Database.")
    exit()


root = Tk()
root.config(bg=BG)
btn_sign_up_root                    = Button(root, cnf=CNF_BTNS, text='Sign Up', command=lambda:change_window(root, sign_up_window))
btn_login_root                      = Button(root, cnf=CNF_BTNS, text='Login', command=lambda:change_window(root, login_window))
btn_sign_up_root                    .grid(row=1, column=1, cnf=CNF_BTNS_GRID)
btn_login_root                      .grid(row=2, column=1, cnf=CNF_BTNS_GRID)
sign_up_window                      = Toplevel(root, cnf=CNF_WINDOWS)
sign_up_window                      .withdraw()
sign_up_window                      .protocol("WM_DELETE_WINDOW", root.destroy)
label_name_sign_up_window           = Label(sign_up_window, text='Name: ', cnf=CNF_LBLS)
label_surname_sign_up_window        = Label(sign_up_window, text='Sur Name: ', cnf=CNF_LBLS)
label_username_sign_up_window       = Label(sign_up_window, text='Username: ', cnf=CNF_LBLS)
label_password1_sign_up_window      = Label(sign_up_window, text='Password:', cnf=CNF_LBLS)
label_password2_sign_up_window      = Label(sign_up_window, text='Repeat Password: ', cnf=CNF_LBLS)
entry_name_sign_up_window           = Entry(sign_up_window, cnf=CNF_ENTRY)
entry_surname_sign_up_window        = Entry(sign_up_window, cnf=CNF_ENTRY)
entry_username_sign_up_window       = Entry(sign_up_window, cnf=CNF_ENTRY)
entry_password1_sign_up_window      = Entry(sign_up_window, cnf=CNF_ENTRY, show='*')
entry_password2_sign_up_window      = Entry(sign_up_window, cnf=CNF_ENTRY, show='*')
btn_sign_up_sign_up_window          = Button(sign_up_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, text='Sign Up', command=create_account)
btn_back_sign_up_window             = Button(sign_up_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, text='Back', command=lambda:change_window(sign_up_window, root))
label_name_sign_up_window           .grid(row=1, column=1, cnf=CNF_BTNS_GRID)
label_surname_sign_up_window        .grid(row=2, column=1, cnf=CNF_BTNS_GRID)
label_username_sign_up_window       .grid(row=3, column=1, cnf=CNF_BTNS_GRID)
label_password1_sign_up_window      .grid(row=4, column=1, cnf=CNF_BTNS_GRID)
label_password2_sign_up_window      .grid(row=5, column=1, cnf=CNF_BTNS_GRID)
entry_name_sign_up_window           .grid(row=1, column=2, cnf=CNF_BTNS_GRID)
entry_surname_sign_up_window        .grid(row=2, column=2, cnf=CNF_BTNS_GRID)
entry_username_sign_up_window       .grid(row=3, column=2, cnf=CNF_BTNS_GRID)
entry_password1_sign_up_window      .grid(row=4, column=2, cnf=CNF_BTNS_GRID)
entry_password2_sign_up_window      .grid(row=5, column=2, cnf=CNF_BTNS_GRID)
btn_sign_up_sign_up_window          .grid(row=6, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)
btn_back_sign_up_window             .grid(row=6, column=2, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)


login_window                        = Toplevel(root, cnf=CNF_WINDOWS)
login_window                        .withdraw()
login_window                        .protocol("WM_DELETE_WINDOW", root.destroy)
label_username_login_window         = Label(login_window, text='Username: ', cnf=CNF_LBLS)
label_password_login_window         = Label(login_window, text='Password: ', cnf=CNF_LBLS)
entry_username_login_window         = Entry(login_window, cnf=CNF_ENTRY)
entry_password_login_window         = Entry(login_window, cnf=CNF_ENTRY, show='*')
btn_login_login_window              = Button(login_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, text='Login', command=login)
btn_back_login_window               = Button(login_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, text='Back', command=lambda:change_window(login_window, root))
label_username_login_window         .grid(row=1, column=1, cnf=CNF_BTNS_GRID)
label_password_login_window         .grid(row=2, column=1, cnf=CNF_BTNS_GRID)
entry_username_login_window         .grid(row=1, column=2, cnf=CNF_BTNS_GRID)
entry_password_login_window         .grid(row=2, column=2, cnf=CNF_BTNS_GRID)
btn_login_login_window              .grid(row=3, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)
btn_back_login_window               .grid(row=3, column=2, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)

main_window                              = Toplevel(login_window, cnf=CNF_WINDOWS)
main_window                              .withdraw()
main_window                              .protocol("WM_DELETE_WINDOW", root.destroy)
btn_view_orders_main_window_manager      = Button(main_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='View Orders', command=lambda:change_window(main_window, view_orders_window_manager))
btn_view_orders_main_window_user         = Button(main_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='View Orders', command=lambda:change_window(main_window, view_orders_window_user))
btn_add_update_delete_game_main_window   = Button(main_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Add/Update/Delete a Game', command=lambda:change_window(main_window, add_update_delete_window))
btn_search_games_main_window             = Button(main_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Search Games', command=lambda:change_window(main_window, search_window))
btn_logout_main_window                   = Button(main_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Logout', command=lambda:change_window(main_window, login_window))
# btn_view_orders_main_window_manager      .grid(row=1, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)
# btn_view_orders_main_window_user         .grid(row=1, column=2, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)
# btn_add_update_delete_game_main_window   .grid(row=2, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)
btn_search_games_main_window             .grid(row=3, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)
btn_logout_main_window                   .grid(row=4, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)

search_window                       = Toplevel(main_window, cnf=CNF_WINDOWS)
search_window                       .withdraw()
search_window                       .protocol("WM_DELETE_WINDOW", root.destroy)
label_name_search_window            = Label(search_window, text='Name: ', cnf=CNF_LBLS)
label_company_search_window         = Label(search_window, text='Company: ', cnf=CNF_LBLS)
label_date_search_window            = Label(search_window, text='Date:', cnf=CNF_LBLS)
label_price_min_search_window       = Label(search_window, text='Minimum Price: ', cnf=CNF_LBLS)
label_price_max_search_window       = Label(search_window, text='Maximum Price: ', cnf=CNF_LBLS)
label_genre_search_window           = Label(search_window, text='Genre: ', cnf=CNF_LBLS)
label_age_range_search_window       = Label(search_window, text='Age Range: ', cnf=CNF_LBLS)
entry_name_search_window            = Entry(search_window, cnf=CNF_ENTRY)
entry_company_search_window         = Entry(search_window, cnf=CNF_ENTRY)
entry_date_search_window            = Entry(search_window, cnf=CNF_ENTRY)
entry_price_min_search_window       = Entry(search_window, cnf=CNF_ENTRY)
entry_price_max_search_window       = Entry(search_window, cnf=CNF_ENTRY)
entry_genre_search_window           = Entry(search_window, cnf=CNF_ENTRY)
entry_age_range_search_window       = Entry(search_window, cnf=CNF_ENTRY)
btn_search_search_window            = Button(search_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Search Games', command=None)
btn_order_search_window             = Button(search_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Order Game', command=None)
btn_back_search_window              = Button(search_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Back', command=lambda:change_window(search_window, main_window))
label_name_search_window            .grid(row=1, column=1)
label_company_search_window         .grid(row=2, column=1)
label_date_search_window            .grid(row=3, column=1)
label_price_min_search_window       .grid(row=4, column=1)
label_price_max_search_window       .grid(row=5, column=1)
label_genre_search_window           .grid(row=6, column=1)
label_age_range_search_window       .grid(row=7, column=1)
entry_name_search_window            .grid(row=1, column=2)
entry_company_search_window         .grid(row=2, column=2)
entry_date_search_window            .grid(row=3, column=2)
entry_price_min_search_window       .grid(row=4, column=2)
entry_price_max_search_window       .grid(row=5, column=2)
entry_genre_search_window           .grid(row=6, column=2)
entry_age_range_search_window       .grid(row=7, column=2)
btn_search_search_window            .grid(row=8, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)
btn_order_search_window             .grid(row=8, column=2, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)
btn_back_search_window              .grid(row=9, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)



add_update_delete_window                       = Toplevel(main_window, cnf=CNF_WINDOWS)
# add_update_delete_window                       .withdraw()
add_update_delete_window                       .protocol("WM_DELETE_WINDOW", root.destroy)
label_name_add_update_delete_window            = Label(add_update_delete_window, text='Name: ', cnf=CNF_LBLS)
label_company_add_update_delete_window         = Label(add_update_delete_window, text='Company: ', cnf=CNF_LBLS)
label_date_add_update_delete_window            = Label(add_update_delete_window, text='Year:', cnf=CNF_LBLS)
label_price_add_update_delete_window           = Label(add_update_delete_window, text='Price: ', cnf=CNF_LBLS)
label_genre_add_update_delete_window           = Label(add_update_delete_window, text='Genre: ', cnf=CNF_LBLS)
label_age_range_add_update_delete_window       = Label(add_update_delete_window, text='Age Range: ', cnf=CNF_LBLS)
entry_name_add_update_delete_window            = Entry(add_update_delete_window, cnf=CNF_ENTRY)
entry_company_add_update_delete_window         = Entry(add_update_delete_window, cnf=CNF_ENTRY)
entry_date_add_update_delete_window            = Entry(add_update_delete_window, cnf=CNF_ENTRY)
entry_price_add_update_delete_window           = Entry(add_update_delete_window, cnf=CNF_ENTRY)
entry_genre_add_update_delete_window           = Entry(add_update_delete_window, cnf=CNF_ENTRY)
entry_age_range_add_update_delete_window       = Entry(add_update_delete_window, cnf=CNF_ENTRY)
btn_insert_add_update_delete_window            = Button(add_update_delete_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Insert Game', command=create_game)
btn_update_add_update_delete_window            = Button(add_update_delete_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Update Game', command=None)
btn_delete_add_update_delete_window            = Button(add_update_delete_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Delete Game', command=None)
btn_reset_add_update_delete_window             = Button(add_update_delete_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Reset', command=None)
btn_back_add_update_delete_window              = Button(add_update_delete_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Back', command=lambda:change_window(add_update_delete_window, main_window))
btn_search_add_update_delete_window            = Button(add_update_delete_window, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Search', command=None)
label_name_add_update_delete_window            .grid(row=1, column=1)
label_company_add_update_delete_window         .grid(row=2, column=1)
label_date_add_update_delete_window            .grid(row=3, column=1)
label_price_add_update_delete_window           .grid(row=4, column=1)
label_genre_add_update_delete_window           .grid(row=5, column=1)
label_age_range_add_update_delete_window       .grid(row=6, column=1)
entry_name_add_update_delete_window            .grid(row=1, column=2)
entry_company_add_update_delete_window         .grid(row=2, column=2)
entry_date_add_update_delete_window            .grid(row=3, column=2)
entry_price_add_update_delete_window           .grid(row=4, column=2)
entry_genre_add_update_delete_window           .grid(row=5, column=2)
entry_age_range_add_update_delete_window       .grid(row=6, column=2)
btn_insert_add_update_delete_window            .grid(row=7, column=1)
btn_update_add_update_delete_window            .grid(row=7, column=2)
btn_delete_add_update_delete_window            .grid(row=8, column=1)
btn_reset_add_update_delete_window             .grid(row=8, column=2)
btn_back_add_update_delete_window              .grid(row=9, column=1)
btn_search_add_update_delete_window              .grid(row=9, column=2)

view_orders_window_manager          = Toplevel(login_window, cnf=CNF_WINDOWS)
view_orders_window_manager          .withdraw()
view_orders_window_manager          .protocol("WM_DELETE_WINDOW", root.destroy)
btn_back_view_orders_window_manager = Button(view_orders_window_manager, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Back', command=lambda:change_window(view_orders_window_manager, main_window))
btn_back_view_orders_window_manager .grid(row=1, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)

view_orders_window_user          = Toplevel(login_window, cnf=CNF_WINDOWS)
view_orders_window_user          .withdraw()
view_orders_window_user          .protocol("WM_DELETE_WINDOW", root.destroy)
btn_back_view_orders_window_user = Button(view_orders_window_user, cnf=CNF_BTNS_SIGN_UP_WINDOW, width=24, text='Back', command=lambda:change_window(view_orders_window_user, main_window))
btn_back_view_orders_window_user .grid(row=1, column=1, cnf=CNF_BTNS_SIGN_UP_WINDOW_GRID)


mainloop()
