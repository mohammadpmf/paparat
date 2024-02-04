from random import choice

choices = ['r', 'p', 's']
computer_choice = choice(choices)
message = f"Choose from {choices}: "
user_choice=input(message)
if user_choice not in choices:
    user_choice=input(message)

if computer_choice==user_choice:
    print("It's a tie!")
elif (computer_choice, user_choice) in [('r', 's'), ('s', 'p'), ('p', 'r')]:
    print("You lose")
else:
    print("You win")
print(f"{computer_choice=}, {user_choice=}")