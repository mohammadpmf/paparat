import string
import os
os.system('cls')

real_password = "5"

found=False
letters = string.ascii_lowercase+string.digits
for i in letters:
    for j in letters:
        for k in letters:
            for t in letters:
                for r in letters:
                    guess = i+j+k+t+r
                    if guess==real_password:
                        print(f'password is {guess}')
                        found=True
                        break
                if found==True:
                    break
            if found==True:
                break
        if found==True:
            break
    if found==True:
        break
        