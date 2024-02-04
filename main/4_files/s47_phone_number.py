import json

def save():
    f = open('main/4_files/contacts.txt', 'w')
    f.write(str(contacts))
    f.close()

def save2():
    f = open('main/4_files/contacts2.txt', 'w')
    for name, number in contacts.items():
        f.write(f"{name}\n{number}\n")
    f.close()

def load():
    try:
        f = open('main/4_files/contacts.txt', 'r')
        contacts = f.read()
        f.close()
    except FileNotFoundError:
        return {}
    contacts = contacts.replace('{', '')
    contacts = contacts.replace('}', '')
    contacts = contacts.replace('\'', '')
    contacts = contacts.replace(':', '')
    contacts = contacts.split(',')
    new_dict = {}
    for item in contacts:
        temp = item.strip().split()
        name = temp[0]
        number = temp[1]
        new_dict[name]=number
    return new_dict

def load2():
    try:
        new_dict = {}
        f = open('main/4_files/contacts2.txt', 'r')
        while True:
            name = f.readline().strip()
            if name == "":
                break
            number = f.readline().strip()
            new_dict[name]=number
        f.close()
    except FileNotFoundError:
        return {}
    return new_dict

def save3():
    f = open('main/4_files/contacts3.json', 'w')
    json.dump(contacts, f, indent=4)
    f.close()

def load3():
    try:
        f = open('main/4_files/contacts3.json', 'r')
        contacts = json.load(f)
        return contacts
    except FileNotFoundError:
        return {}
    
contacts = load3()

while True:
    name = input("Enter name: ").capitalize()
    if name == "0":
        break
    if name in contacts:
        print(contacts.get(name))
        # print(contacts[name])
    else:
        answer = input("This contact is not in your contact list.\nDo you want to add him/her?").lower()
        while answer not in ["yes", "y", "no", "n"]:
            answer = input("This contact is not in your contact list.\nDo you want to add him/her?").lower()
        if answer in ["yes", "y"]:
            number = input("Enter his/her number: ")
            contacts[name]=number
            # contacts.update({name:number})

save3()