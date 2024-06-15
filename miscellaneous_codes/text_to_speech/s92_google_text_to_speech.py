# from gtts import gTTS
# import playsound
# def speak(t):
#     s = gTTS(text=t, lang='en')
#     f = "1.mp3"
#     s.save(f)
#     playsound.playsound(f)

# speak('salam')
# # speak('سلام علیکم')

from gtts import gTTS
from io import BytesIO
from pygame import mixer
import time

def speak(t):
    mp3_fp = BytesIO()
    tts = gTTS(t, lang='ar')
    tts.write_to_fp(mp3_fp)
    return mp3_fp

mixer.init()
# sound = speak('hello, Welcome to Python Text-to-Speech!')
sound = speak('دوسِتون دارَم. لایک و فالو یادِتون نَرِ')
sound.seek(0) # زمان به ده هزارم ثانیه. یعنی اگه میخواید از ثانیه ۲ پخش بشه به جای 0 بنویسید 20000
mixer.music.load(sound, "mp3")
mixer.music.play()
time.sleep(5)