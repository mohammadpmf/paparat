def generate_numbers_and_sum(num):
    global total
    for i in range(1, num + 1):
        total += i
        yield i

total = 0
for num in generate_numbers_and_sum(100):
    # print(f"sum is: {total}")
    # print(f"Generated number: {num}")
    pass
print(total)