import os
# res = os.system(f"rar x -p1234 \"hack/3.rar\"")
# print(res)
numbers='0123456789'

for i1 in numbers:
    for i2 in numbers:
        for i3 in numbers:
            for i4 in numbers:
                    guess = i1+i2+i3+i4
                    res = os.system(f"rar x -p{guess} \"hack/p.rar\"")
                    print(res)
