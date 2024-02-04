from string import ascii_uppercase
d = {}
for index, character in enumerate(ascii_uppercase):
    d[index+10]=character
d2 = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J',
    20: 'K',
    21: 'L',
    22: 'M',
    23: 'N',
    24: 'O',
    25: 'P',
    26: 'Q',
    27: 'R',
    28: 'S',
    29: 'T',
    30: 'U',
    31: 'V',
    32: 'W',
    33: 'X',
    34: 'Y',
    35: 'Z',
}
def mabna_n(a: int, n: int=2) -> str:
    result = ""
    while a!=0:
        a, t = divmod(a, n)
        if t>=10:
            t = d[t]
        result += str(t)
    return result[::-1]


a = int(input("Enter a number: "))
n = int(input("Enter mabna: "))
b = mabna_n(a, n)
print(b)