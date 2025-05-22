# def decorator(func):
#     def wrapper():
#         print(1)
#         print(2)
#         func()
#         print(3)
#         print(4)
#     return wrapper

# def print1():
#     print("Print1")
# def print2():
#     print("Print2")

# @decorator
# def print3():
#     print("Print3")

# print3()
# test(print3)

from datetime import datetime
def time_decorator(func):
    def wrapper(*args, **kwargs):
        print(datetime.now())
        return func(*args, **kwargs)
    return wrapper


def login_required(func):
    def wrapper(*args, **kwargs):
        u = input("Enter username: ")
        p = input("Enter password: ")
        if (u, p) == ("admin", "admin"):
            return func(*args, **kwargs)
        else:
            return "You need to Login first."
    return wrapper
