from tkinter import *
from tkinter import filedialog, messagebox
import pygame
from PIL import Image, ImageTk
from threading import Thread
from time import sleep

BG = "#333333"
FG = 'orange'
BTN_SIZE = 128
BTN_CONFIG = {
    'font': ('', 24),
    'padx': 8,
    'pady': 8
}

class MusicPlayer():
    '''
    This music player uses pygame and pillow.
    You should install them using pip install pygame and pip install pillow
    The main Tk window is mandetory.
    For using this MusicPlayer, you can use 3 images for the play, pause and stop button, but
    notice that you should choose all of them, ohterwise, you will see 'play', 'pause' and 'stop' texts.
    Enjoy it :)
    '''

    def __init__(
            self,
            root, 
            sound_volume=50,
            bg=BG,
            fg=FG,
            play_image_address=None,
            pause_image_address=None,
            stop_image_address=None,
            title = "My Pourmohammadi Fallah's Music Player"
            ):
        self.root = root
        self.title=title
        self.bg=bg
        self.fg=fg
        if sound_volume>100:
            sound_volume=100
        elif sound_volume<0:
            sound_volume=0

        self.sound_volume = sound_volume
        self.is_first_click = True
        self.is_playing = False
        self.playing_time = 0
        self.file_name = ""
        self.lenght_of_music = 0

        pygame.mixer.init()
        self.player = pygame.mixer.music
        self.player.set_volume(self.sound_volume/100)
        
        self.frame_music_player  = LabelFrame(self.root, bg=self.bg, fg=self.fg, text=self.title)
        self.play_image_address  = play_image_address
        self.pause_image_address = pause_image_address
        self.stop_image_address  = stop_image_address
        if self.play_image_address != None and self.pause_image_address != None and self.stop_image_address != None:
            self.img_play            = Image.open(self.play_image_address)
            self.img_pause           = Image.open(self.pause_image_address)
            self.img_stop            = Image.open(self.stop_image_address)
            self.img_play            = self.img_play.resize((BTN_SIZE-10, BTN_SIZE-10))
            self.img_pause           = self.img_pause.resize((BTN_SIZE-10, BTN_SIZE-10))
            self.img_stop            = self.img_stop.resize((BTN_SIZE-10, BTN_SIZE-10))
            self.img_play            = ImageTk.PhotoImage(self.img_play)
            self.img_pause           = ImageTk.PhotoImage(self.img_pause)
            self.img_stop            = ImageTk.PhotoImage(self.img_stop)
            self.btn_browse          = Button(self.frame_music_player, cnf=BTN_CONFIG, bg=self.bg, fg=self.fg, activebackground=self.fg, activeforeground=self.bg, text="...", command=self.load_music)
            self.btn_play_pause      = Button(self.frame_music_player, cnf=BTN_CONFIG, bg=self.bg, fg=self.fg, activebackground=self.fg, activeforeground=self.bg, image=self.img_play, command=self.play_pause)
            self.btn_stop            = Button(self.frame_music_player, cnf=BTN_CONFIG, bg=self.bg, fg=self.fg, activebackground=self.fg, activeforeground=self.bg, image=self.img_stop, command=self.stop)
        else:
            self.btn_browse          = Button(self.frame_music_player, cnf=BTN_CONFIG, bg=self.bg, fg=self.fg, activebackground=self.fg, activeforeground=self.bg, text="...", command=self.load_music)
            self.btn_play_pause      = Button(self.frame_music_player, cnf=BTN_CONFIG, bg=self.bg, fg=self.fg, activebackground=self.fg, activeforeground=self.bg, text="Play", command=self.play_pause)
            self.btn_stop            = Button(self.frame_music_player, cnf=BTN_CONFIG, bg=self.bg, fg=self.fg, activebackground=self.fg, activeforeground=self.bg, text="Stop", command=self.stop)
        self.lbl_sound           = Label(self.frame_music_player, bg=self.bg, fg=self.fg, text="Change Sound")
        self.scale_sound         = Scale(self.frame_music_player, activebackground=self.fg, bg=self.bg, fg=self.fg, highlightbackground=self.bg, troughcolor=self.bg, orient='horizontal', from_=0, to=100, command=self.change_volume)
        self.lbl_passed_time     = Label(self.frame_music_player, bg=self.bg, fg=self.fg, text="Choose point")
        self.scale_passed_time   = Scale(self.frame_music_player, activebackground=self.fg, bg=self.bg, fg=self.fg, highlightbackground=self.bg, troughcolor=self.bg, orient='horizontal', from_=0, command=self.play_from_here)
        self.scale_sound        .set(self.sound_volume)  
        self.scale_passed_time .bind('<ButtonRelease-1>', self.manage_it)
        self.btn_browse        .place(x=10*1+BTN_SIZE*0,     y=10,                       width=BTN_SIZE,         height=BTN_SIZE         )
        self.btn_play_pause    .place(x=10*2+BTN_SIZE*1,     y=10,                       width=BTN_SIZE,         height=BTN_SIZE         )
        self.btn_stop          .place(x=10*3+BTN_SIZE*2,     y=10,                       width=BTN_SIZE,         height=BTN_SIZE         )
        self.scale_sound       .place(x=10*1+BTN_SIZE*1,     y=10+BTN_SIZE,              width=BTN_SIZE*2+10*3,  height=BTN_SIZE/2       )
        self.lbl_sound         .place(x=10*1+BTN_SIZE*0,     y=10+BTN_SIZE,              width=BTN_SIZE,         height=BTN_SIZE/2       )
        self.scale_passed_time .place(x=10*1+BTN_SIZE*1,     y=10+BTN_SIZE+BTN_SIZE/2,   width=BTN_SIZE*2+10*3,  height=BTN_SIZE/2       )
        self.lbl_passed_time   .place(x=10*1+BTN_SIZE*0,     y=10+BTN_SIZE+BTN_SIZE/2,   width=BTN_SIZE,         height=BTN_SIZE/2       )

    def update_passed_time(self):
        while True:
            while self.is_playing:
                self.playing_time+=1
                self.scale_passed_time.set(self.playing_time)
                print("Playing:", self.playing_time)
                sleep(1)
            while not self.is_playing:
                self.playing_time=self.player.get_pos()
                print("Paused:", self.playing_time)
                sleep(1)

    def load_music(self):
        self.temp = filedialog.askopenfilename()
        if self.temp in ["", None, ()]:
            return
        self.file_name = self.temp
        self.scale_passed_time.set(0)
        self.is_playing=False
        self.playing_time=0
        if self.play_image_address == None:
            self.btn_play_pause.config(text='Play')
        else:
            self.btn_play_pause.config(image=self.img_play)
        self.player.load(self.file_name)
        self.temp = pygame.mixer.Sound(self.file_name)
        self.lenght_of_music = round(self.temp.get_length())
        self.scale_passed_time.config(to=self.lenght_of_music)
        self.player.play()
        self.player.pause()

    def play_pause(self):
        if self.file_name in ["", None, ()]:
            messagebox.showerror("Error", "You must choose an audio file first!")
            return
        if self.is_playing==True:
            self.is_playing=False
            self.player.pause()
            self.playing_time=round(self.player.get_pos()/1000)
            if self.play_image_address == None:
                self.btn_play_pause.config(text='Play')
            else:
                self.btn_play_pause.config(image=self.img_play)
        else:
            self.is_playing=True
            if self.pause_image_address == None:
                self.btn_play_pause.config(text='Pause')
            else:
                self.btn_play_pause.config(image=self.img_pause)
            self.playing_time=round(self.scale_passed_time.get())
            self.player.set_pos(self.playing_time)
            self.player.unpause()
            # self.player.play(start=self.playing_time)
            if self.is_first_click:
                self.is_first_click = False
                self.th1 = Thread(target=self.update_passed_time, daemon=True)
                self.th1.start()
            
    def stop(self):
        if self.lenght_of_music>0:
            self.player.stop()
            self.player.play()
            self.player.pause()
        self.scale_passed_time.set(0)
        self.is_playing=False
        self.playing_time=0
        if self.play_image_address == None:
            self.btn_play_pause.config(text='Play')
        else:
            self.btn_play_pause.config(image=self.img_play)

    def change_volume(self, event):
        self.sound_volume=int(event)
        self.player.set_volume(self.sound_volume/100)

    def manage_it(self, event):
        if self.is_playing:
            # self.player.play(start=self.playing_time)
            self.player.set_pos(self.playing_time)

    def play_from_here(self, event):
        if self.lenght_of_music>0:
            self.playing_time = int(event)
            self.scale_passed_time.set(self.playing_time)

    def place(self, x=10*1, y=10, width=BTN_SIZE*3+10*5, height=10*4+BTN_SIZE*2):
        self.frame_music_player.place(x=x, y=y, width=width, height=height,)

if __name__=="__main__":
    root = Tk()
    root.geometry('1000x400+100+100')
    mplayer = MusicPlayer(
        root,
        play_image_address='main/7_tkinter/music_player/play.png',
        pause_image_address='main/7_tkinter/music_player/pause.png',
        stop_image_address='main/7_tkinter/music_player/stop.jpg'
        )
    mplayer.place()
    root.mainloop()