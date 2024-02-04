import os
os.system('cls')
username = input("Enter username: ")
password = input("Enter password: ")
password2 = input("Repeat password: ")
if (password in username) or (username in password):
    print("Password and username can not be subset of each other.\nAccount did not create.")
elif len(password)<=8:
    print("Password can not be less than or equal 8 characters.\nAccount did not create.")
elif password.islower():
    print("Password should have at least one capital letter.\nAccount did not create.")
elif password.isupper():
    print("Password should have at least one lower case letter.\nAccount did not create.")
elif password.isalpha():
    print("Password should have at least one digit.\nAccount did not create.")
elif password != password2:
    print("Two passwords does not match.\nAccount did not create.")
else:
    print("Account created successfully!")
