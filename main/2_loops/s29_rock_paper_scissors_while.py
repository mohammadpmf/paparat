from random import choice

choices = ['r', 'p', 's']
message = f"Choose from {choices}: "

user_wins = 0
computer_wins = 0
draw = 0
while True:
    computer_choice = choice(choices)
    user_choice=input(message)
    while user_choice not in choices:
        user_choice=input(message)
    if computer_choice==user_choice:
        print("It's a tie!")
        draw += 1
    elif (computer_choice, user_choice) in [('r', 's'), ('s', 'p'), ('p', 'r')]:
        print("You lose")
        computer_wins += 1
    else:
        print("You win")
        user_wins += 1
    print(f"{computer_choice=}, {user_choice=}")
    answer = input("Want to play again?(y/n)")
    while answer not in ['y','n']:
        answer = input("Want to play again?(y/n)")
    if answer=='n':
        break

print(f"{user_wins=:<12}\t{computer_wins=:<12}\t{draw=:<10}")