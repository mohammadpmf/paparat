# from turtle import *
# from math import sqrt

# speed(0)
# for j in range(10, 400, 10):
#     up()
#     goto(-j/2, -j*sqrt(3)/2)
#     down()
#     for i in range(5):
#         fd(j)
#         lt(360/6)

# for j in range(1, 200,2):
#     for i in range(150):
#         fd(i)
#         lt(i)

# done()

for i in range(1, 21):
    for j in range(1, 21):
        print(f"{i*j:3}", end=' ')
    print()