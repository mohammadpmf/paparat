def hanoi(n, avvali, akhari, komaki):
    if n>0:
        hanoi(n-1, avvali, komaki, akhari)
        print(f"{n}-->{akhari}")
        hanoi(n-1, komaki, akhari, avvali)

# hanoi(64, 1, 3, 2)
print(2**64-1)