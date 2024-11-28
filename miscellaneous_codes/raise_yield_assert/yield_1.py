def simple_generator():
    yield 1
    print(1)
    print(2)
    print(3)
    print(5555)
    yield 2
    print(6666)
    yield 3
    yield "reza"
    yield 2.3
    yield True
    yield 4
    print(7777)
    yield 5
    return
    yield 7
    yield 8
    yield 9
    yield 10

for value in simple_generator():
    print(value)