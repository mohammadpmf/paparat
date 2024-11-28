def simple_generator():
    yield 1
    yield 2
    yield 3
    yield "reza"
    yield 2.3
    yield True
    yield 4
    yield 5
    return
    yield 7
    yield 8
    yield 9
    yield 10

for value in simple_generator():
    print(value)