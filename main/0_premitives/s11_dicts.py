# foods = ['pizza', 'soosis', 'hamberger', 'pasta', 'hotdog', 'sibzamini']
# prices = [120000, 80000, 90000, 130000, 85000, 75000]

# print(foods[4], prices[4])

# foods = {
#     'pizza': 120000,
#     'soosis': 80000,
#     'hamberger': 90000,
#     'pasta': 130000,
#     'hotdog': 85000,
#     'sibzamini': 75000,
# }
contacts = {
    'ali': '09112345698',
    'reza': '09125487453',
}
# contacts.clear()
# contacts2 = contacts.copy()
# contacts2['ali'] = '0'
# print(contacts.get('ali'))
# print(contacts.items())
# number = contacts.pop('ali')
# print(number)
# item = contacts.popitem()
# print(item)
# contacts.update({'hasan': '123'})
# contacts.setdefault('ali','123')
names = ['ali', 'neda', 'hasan', 'sara']
contacts = contacts.fromkeys(names, 0)
print(contacts)
