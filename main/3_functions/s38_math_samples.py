from math import pi, sqrt

def fact(n:int) -> int:
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def get_volume(r:float, h:float) -> float:
    volume = pi*r**2*h
    volume = round(volume, 2)
    return volume

def get_second_equation_answers(a:float, b:float, c:float) -> (float, float):
    delta = b**2-4*a*c
    if delta < 0:
        return "This equation has no real answers!"
    elif delta == 0:
        x1=x2=-b/2*a
    else:
        x1 = (-b+sqrt(delta))/(2*a)
        x2 = (-b-sqrt(delta))/(2*a)
    return x1, x2

def get_area(a:float, b:float, c:float) -> float | str:
    if a+b<c or a+c<b or b+c<a:
        return "This triangle does not exsits!"
    p = (a+b+c)/2
    m = p*(p-a)*(p-b)*(p-c)
    area = sqrt(m)
    return area

print(get_area(15,20,25))

# print(fact(4))
# print(get_volume(10, 10))
# print(get_second_equation_answers(10, 20, 5))

