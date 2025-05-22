from decorators import time_decorator, login_required


@time_decorator
def mul(a, b):
    return a*b

@time_decorator
def add(a, b):
    return a+b

@login_required
def sub(a, b):
    return a-b

def div(a, b):
    return a/b


print(sub(3, 8))