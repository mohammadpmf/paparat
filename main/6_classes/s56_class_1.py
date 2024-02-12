class Person:
    def __init__(self, name="Reza", surname="Alavi", father_name="Ahmad",phone_number="09321456897", nat_code="1234567890"):
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.phone_number = phone_number
        self.nat_code = nat_code
    
    def __str__(self):
        return f"Name: {self.name} {self.surname}\nFather Name: {self.father_name}\nPhone Number: {self.phone_number}\nNational Code: {self.nat_code}"

p1 = Person()
p2 = Person("MohammadReza", "Alavi", "Ahmad", "093214598715", "0123456789")
p3 = Person("Ali", phone_number="09321456891", nat_code="1234567895")
print(p1)
# print(p2.get_info())
# print(p1.name)
# print(p2.name)
# print(p3.father_name)
