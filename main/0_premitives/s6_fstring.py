name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))

print("Hello",name,surname+". You are", age, "years old. You will be", age+1, "next year.")
print(f"Hello {name} {surname}. You are {age} years old. You will be {age+1} next year.")
# Hello reza alavi. You are 20 years old. You will be 21 next year.
print("Hello {} {}. You are {} years old. You will be {} next year.".format(name, surname, age,age+1))
