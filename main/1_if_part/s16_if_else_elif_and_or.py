import os
os.system('cls')
# a = input("Enter password 1: ")
# b = input("Enter password 2: ")
# c = input("Enter password 3: ")
# d = input("Enter password 4: ")
# if a == "123" and b=="456" and c=="789" and d=="0":
#     print("Welcome")
# else:
#     print("Wrong Password")
# print("End")

# name = input("Enter your name: ")
# # if name == 'Nick Fury' or name == 'Maria Hill' or name == 'Phill Coulson':
# if name not in ['Nick Fury', 'Maria Hill', 'Phill Coulson']:
#     print("Welcome")
# else:
#     print("Unauthorized")

name = input("Enter your name: ")
password = input("Enter your password: ")
if (name == 'Nick Fury' and password == "N F") or (name == "Maria Hill" and password == "M H") or (name == "Phill Coulson" and password == "P C"):
    print("Welcome")
else:
    print("Unauthorized")
