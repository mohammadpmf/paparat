# 12345 15
# 1154  11
# 956321
# s = 0
# number = input("Enter a number: ")
# for digit in number:
#     s = s+int(digit)
# print(s)

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# s = 0
# for i in range(b):
#     s = s + a
# print(f"{a}*{b}={s}")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
r = a
q = 0
for i in range(1000000000000):
    if r>=b:
        r -= b
        q += 1
    else:
        break
print(f"{a}//{b}={q}")
print(f"{a}%{b}={r}")

