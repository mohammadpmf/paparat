import random
import string

def code_generator():
    length = random.randint(12, 16)
    characters = string.ascii_letters+string.digits
    generated_list = []
    for _ in range(length):
        char = random.choice(characters)
        generated_list.append(char)
    generated_list.append(random.choice(string.punctuation))
    random.shuffle(generated_list)
    generated_code = ''.join(generated_list)
    return generated_code

print(code_generator())