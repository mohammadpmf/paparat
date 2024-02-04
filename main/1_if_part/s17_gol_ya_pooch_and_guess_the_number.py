import os
from random import randint, choice
os.system('cls')
# gol = choice(['left', 'right'])
# user = input("Left or Right?").lower()
# if user == gol:
#     print(f"{10*'-'} Right. You Win {10*'-'}")
# else:
#     print(f"{10*'-'} You lose {10*'-'}")

# a = input("Enter a word: ")
# b = a[::-1]
# if b==a:
#     print(f"{a} is palindrome")
# else:
#     print(f"{a} is not palindrome")

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# if a>b:
#     a, b = b, a
# answer = randint(a, b)
# guess = int(input(f"Guess a number in range({a}, {b})"))
# if guess == answer:
#     print("You win")
# elif guess > answer:
#     print(f"The answer is lower than {guess}")
# elif guess < answer:
#     print(f"The answer is more than {guess}")
# print(answer)

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