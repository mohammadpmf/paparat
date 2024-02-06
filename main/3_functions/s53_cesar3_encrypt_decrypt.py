cesar_3 = {
    'a': 'd',
    'b': 'e',
    'c': 'f',
    'd': 'g',
    'e': 'h',
    'f': 'i',
    'g': 'j',
    'h': 'k',
    'i': 'l',
    'j': 'm',
    'k': 'n',
    'l': 'o',
    'm': 'p',
    'n': 'q',
    'o': 'r',
    'p': 's',
    'q': 't',
    'r': 'u',
    's': 'v',
    't': 'w',
    'u': 'x',
    'v': 'y',
    'w': 'z',
    'x': 'a',
    'y': 'b',
    'z': 'c',
    ' ': '4'
}
cesar_3_decrypt = {
    'd': 'a',
    'e': 'b',
    'f': 'c',
    'g': 'd',
    'h': 'e',
    'i': 'f',
    'j': 'g',
    'k': 'h',
    'l': 'i',
    'm': 'j',
    'n': 'k',
    'o': 'l',
    'p': 'm',
    'q': 'n',
    'r': 'o',
    's': 'p',
    't': 'q',
    'u': 'r',
    'v': 's',
    'w': 't',
    'x': 'u',
    'y': 'v',
    'z': 'w',
    'a': 'x',
    'b': 'y',
    'c': 'z',
    '4': ' '
}


def cesar_3_encrypt(message):
    temp = ""
    for char in message:
        temp += cesar_3.get(char)
    return temp

def cesar_3_decrypt_function(message):
    temp = ""
    for char in message:
        temp += cesar_3_decrypt.get(char)
    return temp

message = input("Enter a message: ")
encrypted_message = cesar_3_encrypt(message)
print(encrypted_message)

# vdodp4kdhow4fkhwruh4lqmd4nkhbol4jduph