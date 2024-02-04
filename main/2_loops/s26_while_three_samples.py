# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# r = a
# q = 0
# while r>=b:
#     q += 1
#     r -= b
# print(f"{a}//{b}={q}")
# print(f"{a}%{b}={r}")

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# temp = b
# s = 0
# while temp>0:
#     s += a
#     temp -= 1
# print(f"{a}*{b}={s}")

s = 0
number = input("Enter a number: ")
index = 0
while index<len(number):
    s += int(number[index])
    index+=1
print(s)
