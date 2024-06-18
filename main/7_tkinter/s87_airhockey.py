from tkinter import *
from PIL import Image, ImageTk
from random import randint
from time import sleep
from threading import Thread

BALL_SIZE = 48
PLAYER_SIZE = 64
TABLE_COLOR = 'dark green'
START_TIME_COLOR = 'white'
start_time = 3
score_red = 0
score_blue = 0
turn = ''


def move_player(event: Event):
    if event.keysym in ['Up', 'Down']:
        y = int(lbl_blue.place_info().get('y'))
        if event.keysym == 'Up':
            y -= 20
            if y<=0:
                y=0
        else:
            y += 20
            if y>=TABLE_HEIGHT-PLAYER_SIZE:
                y=TABLE_HEIGHT-PLAYER_SIZE
        lbl_blue.place(y=y)
    elif event.keysym in ['w', 'W', 's', 'S']:
        y = int(lbl_red.place_info().get('y'))
        if event.keysym in ['w', 'W']:
            y -= 20
            if y<=0:
                y=0
        else:
            y += 20
            if y>=TABLE_HEIGHT-PLAYER_SIZE:
                y=TABLE_HEIGHT-PLAYER_SIZE
        lbl_red.place(y=y)



def move_ball():
    global score_red, score_blue, turn
    if turn not in ['red', 'blue']:
        answer = randint(0, 1)
        if answer==1:
            x_speed = randint(5, 8)
        else:
            x_speed = randint(-8, -5)
    elif turn == 'red':
        x_speed = randint(5, 8)
    elif turn == 'blue':
        x_speed = randint(-8, -5)
    y_speed = randint(-10, 10)
    while True:
        x = int(lbl_ball.place_info().get('x'))
        y = int(lbl_ball.place_info().get('y'))
        if y>TABLE_HEIGHT-BALL_SIZE or y<0:
            y_speed *= -1
        if x<PLAYER_SIZE:
            red_y_up = int(lbl_red.place_info().get('y'))
            red_y_down = red_y_up+PLAYER_SIZE
            if y>=red_y_up-PLAYER_SIZE and y<=red_y_down:
                x_speed = randint(15, 25)
            elif y-BALL_SIZE>red_y_up or y<red_y_down:
                score_blue += 1
                turn = 'red'
                break
        elif x>PLAYER_BLUE_X-BALL_SIZE:
            blue_y_up = int(lbl_blue.place_info().get('y'))
            blue_y_down = blue_y_up+PLAYER_SIZE
            if y>=blue_y_up-PLAYER_SIZE and y<=blue_y_down:
                x_speed = randint(-25, -15)
            elif y-BALL_SIZE>blue_y_up or y<blue_y_down:
                score_red += 1
                turn = 'blue'
                break
        x += x_speed
        y += y_speed
        lbl_ball.place(x=x, y=y)
        sleep(0.03)
    score_message = f"Red: {score_red}       Blue: {score_blue}"
    lbl_start_time.config(text=score_message)
    lbl_start_time.place(x=TABLE_WIDTH//2-5*BALL_SIZE+8, y=TABLE_HEIGHT//2-1.6*BALL_SIZE)
    lbl_ball.place(x=TABLE_WIDTH//2-BALL_SIZE//2, y=TABLE_HEIGHT//2-BALL_SIZE//2, width=BALL_SIZE, height=BALL_SIZE)
    sleep(3)
    lbl_start_time.place_forget()
    if score_red==5 or score_blue==5:
        if score_red == 5:
            message = f"Red Wins"
        else:
            message = f"Blue Wins"
        lbl_start_time.config(text=message)
        lbl_start_time.place(x=TABLE_WIDTH//2-5*BALL_SIZE+8, y=TABLE_HEIGHT//2-1.6*BALL_SIZE)
        lbl_ball.place_forget()
        return
    move_ball()



def start_game():
    Thread(target=move_ball, daemon=True).start()


def count_to_0_and_start():
    global start_time
    for i in range(3):
        sleep(1)
        start_time -= 1
        lbl_start_time.config(text=start_time)
    start_time = 3
    lbl_start_time.place_forget()
    start_game()


root = Tk()
S_WIDTH = root.winfo_screenwidth()
S_HEIGHT = root.winfo_screenheight()
TABLE_WIDTH = S_WIDTH*2//3
TABLE_HEIGHT = S_HEIGHT*2//3
PLAYER_BLUE_X = TABLE_WIDTH-PLAYER_SIZE
# root.state('zoomed')
root.geometry(f'{TABLE_WIDTH}x{TABLE_HEIGHT}+{S_WIDTH//6}+{S_HEIGHT//6}')
root.config(bg=TABLE_COLOR)
root.bind('<Key>', move_player)
img_red  = Image.open(r'C:\Users\Mohammad\Desktop\Zabt Python\python codes\main\7_tkinter\air_hockey\red.png')
img_blue = Image.open(r'C:\Users\Mohammad\Desktop\Zabt Python\python codes\main\7_tkinter\air_hockey\blue.png')
img_ball = Image.open(r'C:\Users\Mohammad\Desktop\Zabt Python\python codes\main\7_tkinter\air_hockey\black.png')
img_red  = img_red.resize((PLAYER_SIZE, PLAYER_SIZE))
img_blue = img_blue.resize((PLAYER_SIZE, PLAYER_SIZE))
img_ball = img_ball.resize((BALL_SIZE, BALL_SIZE))
img_red  = ImageTk.PhotoImage(img_red)
img_blue = ImageTk.PhotoImage(img_blue)
img_ball = ImageTk.PhotoImage(img_ball)
lbl_red  = Label(root, image=img_red, bg=TABLE_COLOR)
lbl_blue = Label(root, image=img_blue, bg=TABLE_COLOR)
lbl_ball = Label(root, image=img_ball, bg=TABLE_COLOR)
lbl_start_time = Label(root, text=start_time, bg=TABLE_COLOR, fg=START_TIME_COLOR, font=('', 30), width=20, justify='center')
lbl_red .place(x=0, y=TABLE_HEIGHT//2-PLAYER_SIZE//2, width=PLAYER_SIZE, height=PLAYER_SIZE)
lbl_blue.place(x=PLAYER_BLUE_X, y=TABLE_HEIGHT//2-PLAYER_SIZE//2, width=PLAYER_SIZE, height=PLAYER_SIZE)
lbl_ball.place(x=TABLE_WIDTH//2-BALL_SIZE//2, y=TABLE_HEIGHT//2-BALL_SIZE//2, width=BALL_SIZE, height=BALL_SIZE)
lbl_start_time.place(x=TABLE_WIDTH//2-5*BALL_SIZE+8, y=TABLE_HEIGHT//2-1.6*BALL_SIZE)
Thread(target=count_to_0_and_start, daemon=True).start()

root.mainloop()