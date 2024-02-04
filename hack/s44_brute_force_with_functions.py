import string
import os
os.system('cls')

def find1():
    for i in letters:
        if i==real_password:
            return i
def find2():
    for i in letters:
        for j in letters:
            guess = i+j
            if guess==real_password:
                return guess
def find3():
    for i in letters:
        for j in letters:
            for k in letters:
                guess = i+j+k
                if guess==real_password:
                    return guess
def find4():
    for i in letters:
        for j in letters:
            for k in letters:
                for t in letters:
                    guess = i+j+k+t
                    if guess==real_password:
                        return guess
def find5():
    for i in letters:
        for j in letters:
            for k in letters:
                for t in letters:
                    for r in letters:
                        guess = i+j+k+t+r
                        if guess==real_password:
                            return guess

real_password = "ali8"
letters = string.ascii_lowercase+string.digits

password = find1()
if password==None:
    password=find2()
if password==None:
    password=find3()
if password==None:
    password=find4()
if password==None:
    password=find5()
print(password)