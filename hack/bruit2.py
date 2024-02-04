f = open("hack/darkc0de.lst", 'r')
password = 'reza'
for i in range(2000000):
    guess = f.readline().strip()
    if guess == password:
        print(f"Password is {guess}")
        exit()

