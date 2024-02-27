# def test(a, b, c):
#     delta = b**2-4*a*c
#     jazr=delta**0.5
#     x1=((-b)+jazr)/(2*a)
#     x2=((-b)-jazr)/(2*a)
#     return x1, x2

# def add3(n):
#     return n+3
# add3 = lambda n:n+3

# def mul(a,b):
#     return a*b
# mul = lambda a,b:a*b

# print(add3(5))

# print((lambda x:x**2)(6))
# print((lambda x:x**3+7*x)(23))

# a=18
# if a>15: print("Great")
# print("Great") if a>15 else print("Fail")
# # if a>15:
# #     print("Great")
# # else:
# #     print("Fail")


# numbers = [1,4,5,7]
# def add_1(number):
# 	return number+1

# addeds = list(map(add_1, numbers))
# kam_shodeha = list(map(lambda n:n-1, numbers))
# print(kam_shodeha)

# new_list = list(map(lambda n:n**2-5, numbers))
# print(new_list)

# scores = [19,18,20,2,19,9,17,8,15]
# def is_more_than_10(score):
# 	if score>=10:
# 		return True
# 	return False

# print(list(filter(is_more_than_10, scores)))

names = ["Mohammad fallah", "Mohammad Rezayi", "Ali Ahmadi", "Mahdi Nadimi", "Naser Vahdati",
		 "Mohammad Alavi", "Amir Razavi"]

def t(name:str):
    return name.title().startswith("Mohammad")


m_list = list(filter(lambda name:name.title().startswith("Mohammad"), names))
print(m_list)