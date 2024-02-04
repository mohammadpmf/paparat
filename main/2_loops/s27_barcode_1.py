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
factor = []
factor_prices = []
answer = input(f"Enter item #{i}: ").strip()
while answer != "":
    if answer in items:
        factor.append(answer)
        factor_prices.append(items.get(answer))
        i += 1
    answer = input(f"Enter item #{i}: ").strip()

factor_with_amount = []
for item in factor:
    temp = factor.count(item)
    if (item, temp) not in factor_with_amount:
        factor_with_amount.append((item, temp))
# print(factor_with_amount)

total = 0
for name, amount in (factor_with_amount):
    p = items.get(name)
    cart.append(f"Item: {name:<20} Price: {p:<8} Amount: {amount:<10} Total: {p*amount:<10}")
    total += p*amount

for row in cart:
    print(row)
print(total)