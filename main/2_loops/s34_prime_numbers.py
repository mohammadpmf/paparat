n = int(input("Enter n: "))
prime_numbers = []
for i in range(2, n+1):
    prime_numbers.append(i)
# prime_numbers = [i for i in range(1, n+1)]
for j in prime_numbers:
    if j**2 < n:
        for i in range(j, (n//j)+1):
            if j*i in prime_numbers:
                prime_numbers.remove(j*i)
    else:
        break

print(prime_numbers)
print(len(prime_numbers))
