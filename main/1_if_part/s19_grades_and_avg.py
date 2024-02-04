import os
os.system('cls')
# 17-20 => A
# 14-17 => B
# 12-14 => C
# 10-12 => D
# 0 -10 => F
# grades = []
# grade = float(input("Enter grade: "))
# grades.append(grade)
# grade = float(input("Enter grade: "))
# grades.append(grade)
# grade = float(input("Enter grade: "))
# grades.append(grade)
# grade = float(input("Enter grade: "))
# grades.append(grade)
# grade = sum(grades)/len(grades)
# if 17<=grade<=20:
#     print("A")
# elif 14<=grade<17:
#     print("B")
# elif 12<=grade<14:
#     print("C")
# elif 10<=grade<12:
#     print("D")
# elif 0<=grade<10:
#     print("F")
mylist = [9,20,18,16,20,17,19,16,14,12,14,13,20]
# mylist = [9,20,18,16,20,17,20,14,14,12,14,13,20,20]
length = len(mylist)
if length%2==1:
    print(mylist[length//2])
else:
    index = length//2
    s = (mylist[index]+mylist[index-1])
    result = s/2
    print(result)
