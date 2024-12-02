from tkinter import Tk, PhotoImage
from PIL import Image, ImageTk
root = Tk()

# raveshe 1 ke faghat file haye ico ro mitoone.
# root.iconbitmap(r'main\7_tkinter\imgs\a.ico')

# raveshe 2 ke file haye png ro mikhoone. vali khode ico ro nemitoone.
# photo = PhotoImage(file = r'main\7_tkinter\imgs\a.png')
# root.iconphoto(False, photo)

# raveshe 3 ke ba pillow hast va kheyli az format ha ro poshtibani mikone.
ico = Image.open(r'main\7_tkinter\imgs\a.jpg')
photo = ImageTk.PhotoImage(ico)
root.iconphoto(False, photo)

root.mainloop()