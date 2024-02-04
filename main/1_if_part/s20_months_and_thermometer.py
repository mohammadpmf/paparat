# list1 = ['Farvardin', 'Ordibehesht', 'Khordad', 'Tir', 'Mordad', 'Shahrivar']
# list2 = ['Mehr', 'Aban', 'Azar', 'Dey', 'Bahman']
# list3 = ['Esfand']
# m = input("Enter month: ").capitalize()
# if m in list1:
#     print(f"{m} is 31 Days.")
# elif m in list2:
#     print(f"{m} is 30 Days.")
# elif m in list3:
#     print(f"{m} is 29 Days.")
# else:
#     print("I cant answer to you.")
from turtle import *
bgcolor('black')
t = Pen()
temp = numinput("Temperatue", "Enter Temperature: ")
if temp >35:
    t.color('red')
elif temp > 30:
    t.color('orange')
elif temp > 20:
    t.color('green')
elif temp > 10:
    t.color('blue')
elif temp > 0:
    t.color('light blue')
else:
    t.color('white')
t.pensize(10)
# t.lt(90)
t.seth(120)
t.fd(temp*3)

done()
