def fact1(n:int) -> int:
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def fact(n:int) -> int:
    if n<2:
        return 1
    return n*fact(n-1)

# 0 1 2 3 4 5 6  7  8  9  10 11  12
# 1 1 2 3 5 8 13 21 34 55 89 144 233
def fibonacci1(n:int) -> int:
    fib = [1, 1]
    for i in range(n-1):
        fib.append(fib[i]+fib[i+1])
    return fib[-1]

def fibonacci(n:int) -> int:
    if n<2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

# print(fact(50))
print(fibonacci(1000))