def cesar_encrypt_decrypt(message, m=3, mode=1):
    temp = ""
    for char in message:
        n = ord(char)
        n += m*mode
        n = chr(n)
        temp += n
    return temp

message = input("Enter a message: ")
result = cesar_encrypt_decrypt(message, 2, -1)
print(result)
