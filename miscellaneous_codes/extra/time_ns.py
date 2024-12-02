from time import time_ns

a = time_ns()
for i in range(1000000):
    pass
b = time_ns()
print(b-a)
a = time_ns()
for i in '0'*1000000:
    pass
b = time_ns()
print(b-a)

