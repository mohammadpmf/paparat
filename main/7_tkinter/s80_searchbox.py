from pmf_searchbox.searchbox import *

root = Tk()
s = Searchbox(root, values=['salam', 'ok', 'mohammad', 'test', 'reza'], font=('', 60))
s.grid(row=1, column=1)

root.mainloop()