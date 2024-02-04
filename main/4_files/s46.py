# write     => w
# append    => a
# read      => r
try:
    f = open('main/4_files/test.txt', 'r')
except FileNotFoundError:
    print("This file does not exist")
    exit()

# for i in range(10):
#     temp=f.readline().strip()
#     print(temp)

print(f.writable())

# f.write("Ali: 9876543210\n")
