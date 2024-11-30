import hashlib


def simple_hash(password:str):
    hashed_password = hashlib.sha384(password.encode())         # 96 raghame hex
    hashed_password = hashed_password.hexdigest()
    return hashed_password


def hash_password(password: str, salt="1"):
    new_password = (password+salt).encode()
    hashed_password = hashlib.sha384(new_password)              # 96 raghame hex
    hashed_password = hashed_password.hexdigest()
    return hashed_password


print('-'*100)
print(simple_hash("mohammad1234"))
print(simple_hash("mohammad1234"))
print(simple_hash("mohammad1234"))
print(simple_hash("mohammad1234"))
print('-'*100)
print(hash_password('mohammad', '1'))
print(hash_password('mohammad', '7'))
print(hash_password('mohammad', '100'))
print(hash_password('mohammad'))
print('-'*100)
