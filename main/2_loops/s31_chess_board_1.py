from turtle import *

x=50
speed(0)
# tracer(False)
up()
back(4*x)
rt(90)
fd(4*x)
lt(90)
down()
for k in range(4):
    for j in range(4):
        for i in range(4):
            fd(x)
            lt(90)
        fd(x)
        begin_fill()
        for i in range(4):
            fd(x)
            lt(90)
        end_fill()
        fd(x)
    back(8*x)
    lt(90)
    fd(x)
    rt(90)
    for j in range(4):
        begin_fill()
        for i in range(4):
            fd(x)
            lt(90)
        fd(x)
        end_fill()
        for i in range(4):
            fd(x)
            lt(90)
        fd(x)
    back(8*x)
    lt(90)
    fd(x)
    rt(90)

done()