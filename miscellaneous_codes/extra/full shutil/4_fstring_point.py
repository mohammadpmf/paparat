# Error
# for character in "C:\Users\Mohammad\Desktop\My own students\3 Radmehr Bozorgi\25\1.py":
#     print(character)

# Correct
# for character in r"C:\Users\Mohammad\Desktop\My own students\3 Radmehr Bozorgi\25\1.py":
#     print(character)

f = open(r"C:\Users\Mohammad\Desktop\My own students\3 Radmehr Bozorgi\25\1.py")
for i in range(6):
    print(f.readline().strip())