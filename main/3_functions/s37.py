# def my_div_mod(a:int, b:int) -> tuple:
#     '''
#     return a//b and a%b if b is not 0
#     if b is 0 then the message can not divide by 0 will be returned
#     '''
#     if b==0:
#         return "can not divide by 0"
#     q = a//b
#     q2 = a%b
#     return q, q2

# result = my_div_mod(9.75, 2)
# my_div_mod()
# print()
# print(result)
# my_div_mod()
# print(divmod(71, 10))

# def my_upper(s:str)->str:
#     return s.upper()

# print(my_upper("reza"))

from string import punctuation
def is_secure(password:str) -> bool:
    if len(password)<8:
        return False
    if password.isupper():
        return False
    if password.islower():
        return False
    if password.isalpha():
        return False
    result = set(punctuation).intersection(set(password))
    if len(result)==0:
        return False
    return True
    # for character in password:
    #     if character in punctuation:
    #         return True
    # return False

for i in range(10):
    p = input("Enter password: ")
    if is_secure(p):
        print(f"{p} is a secure password.")
    else:
        print(f"{p} is not a secure password.")