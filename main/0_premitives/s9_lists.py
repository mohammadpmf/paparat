#            0        1        2       3        4         5            6
mylist = ['pizza', 'water', 'milk', 'butter', 'egg', 'chocolate', 'hamburger']
new_items = ['soosis', 'milk', 'egg', 'chocolate']
# a = input('Enter new item')
# mylist.append(a)
# mylist.insert(10, a)
# mylist.remove('pizza')
# a = mylist.pop()
# mylist.clear()
# b=mylist.copy()
# b.remove('egg')
mylist.extend(new_items)
# a = mylist.count('egg')
# mylist.sort()
# mylist.reverse()
a = mylist.index('egg', 5)
# print(mylist)
print(a)