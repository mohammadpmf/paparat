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
    "width": 5,
    "height": 2,
}
CNF_ENTRY = {
    'bg': bg,
    'fg': fg,
    "font": ('', 24),
    "width": 30,
}
CNF_GRID = {
    'padx': 1,
    'pady': 1,
    'sticky': 'news',
}
CNF_PACK={
    'expand': 1,
    'fill': 'both',
    'side': 'left'
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
    CNF_ENTRY[which]=color
    entry                 .config(cnf=CNF_ENTRY, insertbackground=fg)
    btn_copy              .config(cnf=CNF_BTN)
    if not mode:
        btn_abs_sin       .config(cnf=CNF_BTN)
        btn_reverse_cos   .config(cnf=CNF_BTN)
        btn_sqrt_tan      .config(cnf=CNF_BTN)
        btn_x2_log        .config(cnf=CNF_BTN)
    btn_second            .config(cnf=CNF_BTN)
    btn_mul            .config(cnf=CNF_BTN)
    btn_clear1            .config(cnf=CNF_BTN)
    btn_div               .config(cnf=CNF_BTN)
    btn_clear             .config(cnf=CNF_BTN)
    btn0                  .config(cnf=CNF_BTN)
    btn_minus             .config(cnf=CNF_BTN)
    btn_plus              .config(cnf=CNF_BTN)
    btn00                 .config(cnf=CNF_BTN)
    btn000                .config(cnf=CNF_BTN)
    btn_dot               .config(cnf=CNF_BTN)
    btn_paranthes_open    .config(cnf=CNF_BTN)
    btn_paranthes_close   .config(cnf=CNF_BTN)
    # btn_equal             .config(cnf=CNF_BTN)
    for button in btn_numbers:
        button.config(cnf=CNF_BTN)


root = Tk()
root.geometry('1000x700')
root.minsize(800, 620)
root.maxsize(1200, 800)
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
frame_1         = Frame(root)
frame_2         = Frame(root)
frame_3         = Frame(root)
frame_4         = Frame(root)
frame_5         = Frame(root)

frame_4_left    = Frame(frame_4)
frame_4_right   = Frame(frame_4)

frame_4_left_1  = Frame(frame_4_left)
frame_4_left_2  = Frame(frame_4_left)

frame_1         .pack(side='top', expand=1, fill='both')
frame_2         .pack(side='top', expand=1, fill='both')
frame_3         .pack(side='top', expand=1, fill='both')
frame_4         .pack(side='top', expand=1, fill='both')
frame_5         .pack(side='top', expand=1, fill='both')

frame_4_left    .pack(side='left', expand=1, fill='both')
frame_4_right   .pack(side='right', expand=1, fill='both')

frame_4_left_1  .pack(side='top', expand=1, fill='both')
frame_4_left_2  .pack(side='top', expand=1, fill='both')

entry = Entry(frame_1, cnf=CNF_ENTRY, insertbackground=fg)
btn_copy = Button(frame_1, cnf=CNF_BTN, text='copy', command=copy, padx=20)         
btn_abs_sin = Button(frame_2, cnf=CNF_BTN, text='|X|', command=lambda: my_mixin("abs_sin"))
btn_reverse_cos = Button(frame_2, cnf=CNF_BTN, text='1/X', command=lambda: my_mixin("reverse_cos"))
btn_sqrt_tan = Button(frame_2, cnf=CNF_BTN, text='√X', command=lambda: my_mixin("sqrt_tan"))
btn_x2_log = Button(frame_2, cnf=CNF_BTN, text='X²', command=lambda:my_mixin("x2_log"))
btn_second = Button(frame_2, cnf=CNF_BTN, text='2nd', command=second) 
btn_mul = Button(frame_2, cnf=CNF_BTN, text='*', command=lambda:insert('*'))   
btn_clear1 = Button(frame_2, cnf=CNF_BTN, text='←', command=clear1)            
btn_numbers = []
for i in range(1, 6):
    btn_numbers.append(Button(frame_3, cnf=CNF_BTN, text=i, command=lambda i=i:insert(i)))
    btn_numbers[i-1].pack(expand=1, fill='both', side='left')
btn_div = Button(frame_3, cnf=CNF_BTN, text='/', command=lambda:insert('/'))   
btn_clear = Button(frame_3, cnf=CNF_BTN, text='C', command=clear)         
for i in range(6, 10):
    btn_numbers.append(Button(frame_4_left_1, cnf=CNF_BTN, text=i, command=lambda i=i:insert(i)))
    btn_numbers[i-1].pack(expand=1, fill='both', side='left')
btn0 = Button(frame_4_left_1, cnf=CNF_BTN, text='0', command=lambda:insert('0'))      
btn_minus = Button(frame_4_left_1, cnf=CNF_BTN, text='-', command=lambda:insert('-'))     
btn_plus = Button(frame_4_right, cnf=CNF_BTN, text='+', command=lambda:insert('+'))     

btn00 = Button(frame_4_left_2, cnf=CNF_BTN, text='00', command=lambda:insert('00'))
btn000 = Button(frame_5, cnf=CNF_BTN, text='000', command=lambda:insert('000'))
btn0000 = Button(frame_5, cnf=CNF_BTN, text='0000', command=lambda:insert('0000'))
btn_dot = Button(frame_4_left_2, cnf=CNF_BTN, text='.', command=lambda:insert('.'))     
btn_paranthes_open = Button(frame_4_left_2, cnf=CNF_BTN, text='(', command=lambda:insert('('))     
btn_paranthes_close = Button(frame_4_left_2, cnf=CNF_BTN, text=')', command=lambda:insert(')'))    
btn_equal = Button(frame_4_left_2, cnf=CNF_BTN, text='=', command=equal, bg='green', fg='white', activebackground='lime', activeforeground='white')   


entry                   .pack(cnf=CNF_PACK)
btn_copy                .pack(expand=0, fill='both', side='left')
btn_abs_sin             .pack(cnf=CNF_PACK)
btn_reverse_cos         .pack(cnf=CNF_PACK)
btn_sqrt_tan            .pack(cnf=CNF_PACK)
btn_x2_log              .pack(cnf=CNF_PACK)
btn_second              .pack(cnf=CNF_PACK)
btn_mul                 .pack(cnf=CNF_PACK)
btn_clear1              .pack(cnf=CNF_PACK)
btn_div                 .pack(cnf=CNF_PACK)
btn_clear               .pack(cnf=CNF_PACK)
btn0                    .pack(cnf=CNF_PACK)
btn_minus               .pack(cnf=CNF_PACK)
btn_plus                .pack(cnf=CNF_PACK)
btn00                   .pack(cnf=CNF_PACK)
btn_dot                 .pack(cnf=CNF_PACK)
btn_paranthes_open      .pack(cnf=CNF_PACK)
btn_paranthes_close     .pack(cnf=CNF_PACK)
btn_equal               .pack(cnf=CNF_PACK)
btn000                  .pack(cnf=CNF_PACK)
btn0000                 .pack(cnf=CNF_PACK)

root.mainloop()