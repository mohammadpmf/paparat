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
for k in range(8):
    for j in range(8):
        if (j+k)%2==1:
            begin_fill()
        for i in range(4):
            fd(x)
            lt(90)
        end_fill()
        fd(x)
    bk(8*x)
    lt(90)
    fd(x)
    rt(90)
done()