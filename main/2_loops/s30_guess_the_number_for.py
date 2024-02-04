import os
from random import randint, choice
os.system('cls')

n = int(input("How many times you want to play?"))

for i in range(n):
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    if a>b:
        a, b = b, a
    answer = randint(a, b)
    diff = b-a
    n = diff//10+1
    for i in range(n):
        guess = int(input(f"Guess a number in range({a}, {b})"))
        if guess == answer:
            print("You win")
            break
        elif guess > answer:
            print(f"The answer is lower than {guess}")
        elif guess < answer:
            print(f"The answer is more than {guess}")
    print(answer)