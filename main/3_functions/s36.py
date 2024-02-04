from os import system
system('cls')

def alaki(name, surname, age, address="", father_name="", *args, **kwargs):
    pass

def add_some_number(a=0, b=0, c=0, *args, **kwargs):
    print(kwargs, type(kwargs))
    return a+b+c+sum(args)

print(add_some_number())
print(add_some_number(4,5,6))
print(add_some_number(8,9,10,1,2,3,1,2,5,9,8,7,4,5,1,2,0,1,4,m=5,u=1,k=2,t=3, bgcolor='red', color='orange'))
print(add_some_number(c=20))