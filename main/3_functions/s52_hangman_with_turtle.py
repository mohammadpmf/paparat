import pygame
from turtle import *
from time import sleep
from string import ascii_lowercase
import random


def init_turtle():
    global p1, p2
    p1 = Pen()
    p2 = Pen()
    p1.speed(0)
    p1.ht()
    p1.up()
    p1.goto(0, -250)
    p1.down()
    p2.speed(0)
    p2.pensize(10)
    p2.ht()
    p2.up()
    p2.goto(-450, -250)
    p2.down()
    p2.fd(250)
    p2.lt(90)
    p2.fd(500)
    p2.lt(90)
    p2.fd(100)
    p2.rt(45)
    p2.bk(100*1.41)
    p2.fd(100*1.41)
    p2.lt(45)
    p2.fd(50)
    p2.lt(90)
    p2.fd(100)
    p1.write(''.join(guess), font=('Times', 40), align='center')

def f0():
    global p2
    p2.speed(5)
    p2.rt(90)
    p2.circle(40)
    p2.circle(40, 180)
    p2.rt(90)

def f1():
    global p2
    p2.fd(35)

def f2():
    global p2
    p2.rt(60)
    p2.fd(75)
    p2.bk(75)

def f3():
    global p2
    p2.lt(120)
    p2.fd(75)
    p2.bk(75)
    p2.rt(60)

def f4():
    global p2
    p2.fd(120)

def f5():
    global p2
    p2.rt(45)
    p2.fd(75)
    p2.bk(75)

def f6():
    global p2
    p2.lt(90)
    p2.fd(75)

def correct_turtle():
    global p1
    p1.clear()
    p1.write(''.join(guess), font=('Times', 40), align='center')

def is_finished():
    if "?" not in guess:
        return True
    return False

def correct_guess(c, guess):
    global answer
    number_of_repeat = answer.count(c)
    index = -1
    for i in range(number_of_repeat):
        index = answer.index(c, index+1)
        guess[index]=c
    correct_turtle()
    if is_finished():
        pygame.mixer.Channel(0).play(sound_winner)
        sleep(2)
        exit()

def ask_character():
    i = 0
    while i<7:
        c = textinput("Enter a letter", "Enter a single character: ").lower()
        while len(c) != 1 or c not in list_of_unguessed_characters:
            if len(c) != 1:
                c = textinput("Enter a letter", "Enter exactly a single character: ").lower()
            elif c in list_of_guessed_character:
                c = textinput("Enter an unguessed letter", f"character {c} has been guessed.").lower()
            else:
                c = textinput("Ivalid character", f"character {c} is invalid.").lower()

        if c in answer:
            pygame.mixer.Channel(1).play(sound_right)
            correct_guess(c, guess)
        else:
            pygame.mixer.Channel(1).play(sound_error)
            list_of_functions[i]()
            # eval(f"f{i}")()
            i += 1
        list_of_unguessed_characters.remove(c)
        list_of_guessed_character.append(c)
    pygame.mixer.Channel(0).play(sound_loser)
    textinput("End", f"Game has finished.\nThe answer was {answer}")
    exit()

pygame.mixer.init()
sound_background = pygame.mixer.Sound('main/3_functions/hangman_sounds/background.mp3')
sound_error = pygame.mixer.Sound('main/3_functions/hangman_sounds/error.mp3')
sound_loser = pygame.mixer.Sound('main/3_functions/hangman_sounds/loser.mp3')
sound_winner = pygame.mixer.Sound('main/3_functions/hangman_sounds/winner.mp3')
sound_right = pygame.mixer.Sound('main/3_functions/hangman_sounds/right.mp3')
pygame.mixer.Channel(0).set_volume(0.3)
pygame.mixer.Channel(1).set_volume(0.7)

animals = ['rat', 'rabbit', 'cat', 'cayote', 'peacock', 'rooster', 'hen', 'donkey', 'horse', 'dog', 'mouse']
fruits = ['banana', 'mango', 'apple', 'kiwi', 'orange', 'coconut', 'papaya', 'tangerine', 'potato', 'tomato']
jobs = ['engineer', 'mechanic', 'doctor', 'dentist', 'chef', 'miner', 'nurse', 'programmer', 'teacher']
list_of_categories = ['animals', 'fruits', 'jobs']
list_of_functions = [f0, f1, f2, f3, f4, f5, f6]
list_of_unguessed_characters = list(ascii_lowercase) + [' ']
list_of_guessed_character = []

category = textinput("Choose Category", f"Enter category: {list_of_categories}: ").lower()
while category not in list_of_categories:
    category = textinput("Choose Category", f"Choose from one of these categories: {list_of_categories}: ").lower()
pygame.mixer.Channel(0).play(sound_background)
answer = random.choice(eval(category))
guess = []
for i in answer:
    guess.append('?')

init_turtle()
ask_character()