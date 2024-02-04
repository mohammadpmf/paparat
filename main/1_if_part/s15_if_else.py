import os
os.system('cls')
# >
# >=
# <
# <=
# ==
# !=
# print(18>15)
# print(18>=15)
# print(15>15)
# print(15>=15)
# print(18<15)
# print(18<=15)
# print(15<15)
# print(15<=15)
# print(18==15)
# print(18!=15)
# print(15==15)
# print(15!=15)
# print('hello'=="hello")
# print('hello'=="Hello")
# print('hello'=="Hello".lower())
# print(0.5+0.5==1)
# print(0.1+0.1+0.1==0.3)
# print(0.1+0.1+0.1)
# print(round(25.269))
# print(round(25.269, 2))
# print(0.1+0.1+0.1)
# print(round(0.1+0.1+0.1, 1)==0.3)
# age = int(input("Enter your age: "))
# print(age>18)

is_barbari_open = True
is_sangak_open = False
is_lavash_open = True
if is_barbari_open:
    print('give the money 1')
    print('get 3 breads 1') # barbaries :D
    print('get the cash 1')
else:
    print('go ahead 200 steps.')
    if is_sangak_open:
        print('give the money 2')
        print('get 5 breads 2') # barbaries :D
        print('get the cash 2')
    else:
        print('go ahead 300 steps.')
        if is_lavash_open:
            print('give the money 3')
            print('get 20 breads 3') # barbaries :D
            print('get the cash 3')
        else:
            print("Nowhere is open")
print("End of program")