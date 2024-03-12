from tkinter import *
import pyperclip
import math

REL_WIDTH = 0.137
REL_HEIGHT = 0.19
GAP = 0.005
bg = 'purple'
bg2 = 'red'
fg = 'orange'
mode=False
CNF_BTN = {
    'bg': bg,
    'fg': fg,
    "font": ('', 24),
}


def clear():
    entry.delete(0, END)


def copy():
    pyperclip.copy(entry.get())


def clear1():
    length = len(entry.get())
    entry.delete(length-1, END)


def my_mixin(func):
    global mode
    temp = entry.get().strip()
    clear()
    try:
        temp=eval(temp)
        if (func, mode)==('abs_sin', False):
            result = abs(temp)
        elif (func, mode)==('abs_sin', True):
            result=round(math.sin(math.radians(temp)), 14)
        elif (func, mode)==('reverse_cos', False):
            result = 1/temp
        elif (func, mode)==('reverse_cos', True):
            result=round(math.cos(math.radians(temp)), 14)
        elif (func, mode)==('sqrt_tan', False):
            result = math.sqrt(temp)
        elif (func, mode)==('sqrt_tan', True):
            result=round(math.tan(math.radians(temp)), 14)
        elif (func, mode)==('x2_log', False):
            result = temp**2
        elif (func, mode)==('x2_log', True):
            result=math.log10(temp)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")
    

def equal():
    temp = entry.get()
    clear()
    try:
        temp=eval(temp)
        entry.insert(0, temp)
    except SyntaxError:
        entry.insert(0, "Error")
    except ZeroDivisionError:
        entry.insert(0, "Can not divide by 0 Error")
    except TypeError:
        entry.insert(0, "Error")
    except NameError:
        entry.insert(0, "Error")


def insert(character):
    entry.insert(END, character)


def second():
    global mode
    mode = not mode
    if mode:
        btn_abs_sin.config(text='sin(x)', bg=bg2, fg=fg)
        btn_reverse_cos.config(text='cos(x)', bg=bg2, fg=fg)
        btn_sqrt_tan.config(text='tan(x)', bg=bg2, fg=fg)
        btn_x2_log.config(text='log(x)', bg=bg2, fg=fg)
    else:
        btn_abs_sin.config(text='|X|', bg=bg, fg=fg)
        btn_reverse_cos.config(text='1/X', bg=bg, fg=fg)
        btn_sqrt_tan.config(text='√X', bg=bg, fg=fg)
        btn_x2_log.config(text='X²', bg=bg, fg=fg)


def change_color(which, color):
    global bg, fg, mode
    if which=='bg':
        bg=color
        root.config(bg=bg)
    elif which=='fg':
        fg=color
    CNF_BTN[which]=color
    entry                 .config(cnf=CNF_BTN, insertbackground=fg)
    btn_copy              .config(cnf=CNF_BTN)
    if not mode:
        btn_abs_sin       .config(cnf=CNF_BTN)
        btn_reverse_cos   .config(cnf=CNF_BTN)
        btn_sqrt_tan      .config(cnf=CNF_BTN)
        btn_x2_log        .config(cnf=CNF_BTN)
    btn_second            .config(cnf=CNF_BTN)
    btn_insert            .config(cnf=CNF_BTN)
    btn_clear1            .config(cnf=CNF_BTN)
    btn_div               .config(cnf=CNF_BTN)
    btn_clear             .config(cnf=CNF_BTN)
    btn0                  .config(cnf=CNF_BTN)
    btn_minus             .config(cnf=CNF_BTN)
    btn_plus              .config(cnf=CNF_BTN)
    btn000                .config(cnf=CNF_BTN)
    btn_dot               .config(cnf=CNF_BTN)
    btn_paranthes_open    .config(cnf=CNF_BTN)
    btn_paranthes_close   .config(cnf=CNF_BTN)
    # btn_equal             .config(cnf=CNF_BTN)
    for button in btn_numbers:
        button.config(cnf=CNF_BTN)


root = Tk()
root.geometry('1000x500')
root.minsize(800, 400)
root.maxsize(1200, 600)
menubar = Menu(root)
bg_menu = Menu(menubar, tearoff=0)
fg_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="BG Menus", menu=bg_menu)
menubar.add_cascade(label="FG Menus", menu=fg_menu)
menubar.add_separator()
menubar.add_separator()
menubar.add_command(label='Exit', command=root.destroy)
dark_bg_colors_menu = Menu(bg_menu, tearoff=0)
light_bg_colors_menu = Menu(bg_menu, tearoff=0)
main_bg_colors_menu = Menu(bg_menu, tearoff=0)
secondary_bg_colors_menu = Menu(bg_menu, tearoff=0)
dark_fg_colors_menu = Menu(fg_menu, tearoff=0)
light_fg_colors_menu = Menu(fg_menu, tearoff=0)
main_fg_colors_menu = Menu(fg_menu, tearoff=0)
secondary_fg_colors_menu = Menu(fg_menu, tearoff=0)
bg_menu.add_cascade(label='Dark BG colors menu', menu=dark_bg_colors_menu)
bg_menu.add_cascade(label='Light BG colors menu', menu=light_bg_colors_menu)
bg_menu.add_cascade(label='Main BG colors menu', menu=main_bg_colors_menu)
bg_menu.add_cascade(label='Secondary BG colors menu', menu=secondary_bg_colors_menu)
fg_menu.add_cascade(label='Dark FG colors menu', menu=dark_fg_colors_menu)
fg_menu.add_cascade(label='Light FG colors menu', menu=light_fg_colors_menu)
fg_menu.add_cascade(label='Main FG colors menu', menu=main_fg_colors_menu)
fg_menu.add_cascade(label='Secondary FG colors menu', menu=secondary_fg_colors_menu)

dark_bg_colors_menu.add_command(label ='Black', command = lambda: change_color('bg', 'black'),background='black', foreground='white')
dark_bg_colors_menu.add_command(label ='Deep dark gray', command = lambda: change_color('bg', '#222222'),background='#222222', foreground='white') 
dark_bg_colors_menu.add_command(label ='Dark gray', command = lambda: change_color('bg', '#333333'),background='#333333', foreground='white') 
dark_bg_colors_menu.add_command(label ='Gray', command = lambda: change_color('bg', '#555555'),background='#555555', foreground='white') 
light_bg_colors_menu.add_command(label ='White', command = lambda: change_color('bg', 'white'),background='white')
light_bg_colors_menu.add_command(label ='Deep light gray', command = lambda: change_color('bg', '#eeeeee'),background='#eeeeee') 
light_bg_colors_menu.add_command(label ='light gray', command = lambda: change_color('bg', '#aaaaaa'),background='#aaaaaa') 
main_bg_colors_menu.add_command(label ='red', command = lambda: change_color('bg', 'red'),background='red') 
main_bg_colors_menu.add_command(label ='green', command = lambda: change_color('bg', 'green'),background='green')
main_bg_colors_menu.add_command(label ='blue', command = lambda: change_color('bg', 'blue'),background='blue', foreground='white') 
main_bg_colors_menu.add_command(label ='yellow', command = lambda: change_color('bg', 'yellow'),background='yellow')
secondary_bg_colors_menu.add_command(label ='sky blue', command = lambda: change_color('bg', 'sky blue'),background='sky blue') 
secondary_bg_colors_menu.add_command(label ='purple', command = lambda: change_color('bg', 'purple'),background='purple')
secondary_bg_colors_menu.add_command(label ='orange', command = lambda: change_color('bg', 'orange'),background='orange') 
secondary_bg_colors_menu.add_command(label ='pink', command = lambda: change_color('bg', 'pink'),background='pink') 
secondary_bg_colors_menu.add_command(label ='violet', command = lambda: change_color('bg', 'violet'),background='violet') 
secondary_bg_colors_menu.add_command(label ='tomato', command = lambda: change_color('bg', 'tomato'),background='tomato') 

dark_fg_colors_menu.add_command(label ='Black', command = lambda: change_color('fg', 'black'),background='black', foreground='white')
dark_fg_colors_menu.add_command(label ='Deep dark gray', command = lambda: change_color('fg', '#222222'),background='#222222', foreground='white') 
dark_fg_colors_menu.add_command(label ='Dark gray', command = lambda: change_color('fg', '#333333'),background='#333333', foreground='white') 
dark_fg_colors_menu.add_command(label ='Gray', command = lambda: change_color('fg', '#555555'),background='#555555', foreground='white') 
light_fg_colors_menu.add_command(label ='White', command = lambda: change_color('fg', 'white'),background='white')
light_fg_colors_menu.add_command(label ='Deep light gray', command = lambda: change_color('fg', '#eeeeee'),background='#eeeeee') 
light_fg_colors_menu.add_command(label ='light gray', command = lambda: change_color('fg', '#aaaaaa'),background='#aaaaaa') 
main_fg_colors_menu.add_command(label ='red', command = lambda: change_color('fg', 'red'),background='red') 
main_fg_colors_menu.add_command(label ='green', command = lambda: change_color('fg', 'green'),background='green')
main_fg_colors_menu.add_command(label ='blue', command = lambda: change_color('fg', 'blue'),background='blue', foreground='white') 
main_fg_colors_menu.add_command(label ='yellow', command = lambda: change_color('fg', 'yellow'),background='yellow')
secondary_fg_colors_menu.add_command(label ='sky blue', command = lambda: change_color('fg', 'sky blue'),background='sky blue') 
secondary_fg_colors_menu.add_command(label ='purple', command = lambda: change_color('fg', 'purple'),background='purple')
secondary_fg_colors_menu.add_command(label ='orange', command = lambda: change_color('fg', 'orange'),background='orange') 
secondary_fg_colors_menu.add_command(label ='pink', command = lambda: change_color('fg', 'pink'),background='pink') 
secondary_fg_colors_menu.add_command(label ='violet', command = lambda: change_color('fg', 'violet'),background='violet') 
secondary_fg_colors_menu.add_command(label ='tomato', command = lambda: change_color('fg', 'tomato'),background='tomato') 

root.config(bg=bg, menu=menubar)

entry = Entry(root, cnf=CNF_BTN, insertbackground=fg)
btn_copy = Button(root, cnf=CNF_BTN, text='copy', command=copy)         
btn_abs_sin = Button(root, cnf=CNF_BTN, text='|X|', command=lambda: my_mixin("abs_sin"))
btn_reverse_cos = Button(root, cnf=CNF_BTN, text='1/X', command=lambda: my_mixin("reverse_cos"))
btn_sqrt_tan = Button(root, cnf=CNF_BTN, text='√X', command=lambda: my_mixin("sqrt_tan"))
btn_x2_log = Button(root, cnf=CNF_BTN, text='X²', command=lambda:my_mixin("x2_log"))
btn_second = Button(root, cnf=CNF_BTN, text='2nd', command=second) 
btn_insert = Button(root, cnf=CNF_BTN, text='*', command=lambda:insert('*'))   
btn_clear1 = Button(root, cnf=CNF_BTN, text='←', command=clear1)            
btn_numbers = []
for i in range(1, 6):
    btn_numbers.append(Button(root, cnf=CNF_BTN, text=i, command=lambda i=i:insert(i)))
    btn_numbers[i-1].place(relx=REL_WIDTH*(i-1)+GAP*i, rely=REL_HEIGHT*2+GAP*3, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_div = Button(root, cnf=CNF_BTN, text='/', command=lambda:insert('/'))   
btn_clear = Button(root, cnf=CNF_BTN, text='C', command=clear)         
for i in range(6, 10):
    btn_numbers.append(Button(root, cnf=CNF_BTN, text=i, command=lambda i=i:insert(i)))
    btn_numbers[i-1].place(relx=REL_WIDTH*(i-6)+GAP*(i-5), rely=REL_HEIGHT*3+GAP*4, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn0 = Button(root, cnf=CNF_BTN, text='0', command=lambda:insert('0'))      
btn_minus = Button(root, cnf=CNF_BTN, text='-', command=lambda:insert('-'))     
btn_plus = Button(root, cnf=CNF_BTN, text='+', command=lambda:insert('+'))     

btn000 = Button(root, cnf=CNF_BTN, text='000', command=lambda:insert('000'))
btn_dot = Button(root, cnf=CNF_BTN, text='.', command=lambda:insert('.'))     
btn_paranthes_open = Button(root, cnf=CNF_BTN, text='(', command=lambda:insert('('))     
btn_paranthes_close = Button(root, cnf=CNF_BTN, text=')', command=lambda:insert(')'))    
btn_equal = Button(root, cnf=CNF_BTN, text='=', command=equal, bg='green', fg='white', activebackground='lime', activeforeground='white')   

entry                 .place(relx=REL_WIDTH*0+GAP*1, rely=REL_HEIGHT*0+GAP*1, relwidth=REL_WIDTH*6+GAP*5, relheight=REL_HEIGHT*1+GAP*0)
btn_copy              .place(relx=REL_WIDTH*6+GAP*7, rely=REL_HEIGHT*0+GAP*1, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_abs_sin           .place(relx=REL_WIDTH*0+GAP*1, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_reverse_cos       .place(relx=REL_WIDTH*1+GAP*2, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_sqrt_tan          .place(relx=REL_WIDTH*2+GAP*3, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_x2_log            .place(relx=REL_WIDTH*3+GAP*4, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_second            .place(relx=REL_WIDTH*4+GAP*5, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_insert            .place(relx=REL_WIDTH*5+GAP*6, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_clear1            .place(relx=REL_WIDTH*6+GAP*7, rely=REL_HEIGHT*1+GAP*2, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_div               .place(relx=REL_WIDTH*5+GAP*6, rely=REL_HEIGHT*2+GAP*3, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_clear             .place(relx=REL_WIDTH*6+GAP*7, rely=REL_HEIGHT*2+GAP*3, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn0                  .place(relx=REL_WIDTH*4+GAP*5, rely=REL_HEIGHT*3+GAP*4, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_minus             .place(relx=REL_WIDTH*5+GAP*6, rely=REL_HEIGHT*3+GAP*4, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_plus              .place(relx=REL_WIDTH*6+GAP*7, rely=REL_HEIGHT*3+GAP*4, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*2+GAP*1)
btn000                .place(relx=REL_WIDTH*0+GAP*1, rely=REL_HEIGHT*4+GAP*5, relwidth=REL_WIDTH*2+GAP*1, relheight=REL_HEIGHT*1+GAP*0)
btn_dot               .place(relx=REL_WIDTH*2+GAP*3, rely=REL_HEIGHT*4+GAP*5, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_paranthes_open    .place(relx=REL_WIDTH*3+GAP*4, rely=REL_HEIGHT*4+GAP*5, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_paranthes_close   .place(relx=REL_WIDTH*4+GAP*5, rely=REL_HEIGHT*4+GAP*5, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)
btn_equal             .place(relx=REL_WIDTH*5+GAP*6, rely=REL_HEIGHT*4+GAP*5, relwidth=REL_WIDTH*1+GAP*0, relheight=REL_HEIGHT*1+GAP*0)

root.mainloop()