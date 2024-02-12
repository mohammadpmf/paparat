import pygame

class Car():
    def __init__(self, name, color="black", start="main/6_classes/car_sounds/start2.wav",
                 honk="main/6_classes/car_sounds/honk3.mp3"):
        self.name = name
        self.color = color
        self.start = start
        self.honk = honk

    def honk_f(self):
        sound.load(self.honk)
        sound.play()

    def start_f(self):
        sound.load(self.start)
        sound.play()

pygame.mixer.init()
sound = pygame.mixer.music

car1 = Car("BMW", start="main/6_classes/car_sounds/start1.wav", honk="main/6_classes/car_sounds/honk1.mp3")
car2 = Car("xian", color="yellow")
car3 = Car("benz", honk="main/6_classes/car_sounds/honk2.mp3")

while True:
    answer = input("Which Car?")
    if answer=="1":
        a = input("press 1 to start. 2 to honk: ")
        if a=="1":
            car1.start_f()
        elif a=="2":
            car1.honk_f()
    elif answer=="2":
        a = input("press 1 to start. 2 to honk: ")
        if a=="1":
            car2.start_f()
        elif a=="2":
            car2.honk_f()
    elif answer=="3":
        a = input("press 1 to start. 2 to honk: ")
        if a=="1":
            car3.start_f()
        elif a=="2":
            car3.honk_f()
    
    