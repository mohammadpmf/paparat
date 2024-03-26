cart = []
items = {
    'macaroni': 25000,
    'soya': 25000,
    'nooshabeh': 25000,
    'doogh': 35000,
    'panir': 43000,
    'panir lactiki': 51000,
    'panir bolghari': 69000,
    'pofak': 16000,
    'chips': 18000,
}
i = 1
factor = {}
answer = input(f"Enter item #{i}: ").strip()
while answer != "":
    if answer in items:
        factor.setdefault(answer, 0)
        factor[answer]+=1
        i += 1
    answer = input(f"Enter item #{i}: ").strip()

total = 0
for name, amount in factor.items():
    p = items.get(name)
    cart.append(f"Item: {name:20} Price: {p:<8} Amount: {amount:<10} Total: {p*amount:<10}")
    total += p*amount

for row in cart:
    print(row)
print(total)