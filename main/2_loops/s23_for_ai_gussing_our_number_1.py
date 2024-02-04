import os
from random import randint
os.system('cls')
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
n = 0
guess = randint(a, b)   # 76
for i in range(100):
    s = input(f"Is it {guess}? [>   <   =]")
    n += 1
    if s=='=':
        print("Yey! I found the answer!")
        break
    elif s=='>':
        a = guess+1
        guess=randint(a, b)
    elif s=='<':
        b = guess-1
        guess=randint(a, b)
    else:
        print("I cant understand!")
print(f"I found the answer in {n} times.")