class Person:
    def __init__(self, first_name, last_name, father_name, birth_date, birth_place, national_code,
                 hair_color, eye_color, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.national_code = national_code
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"Salam. I am {self.first_name} {self.last_name}."
    
    def say_hello(self):
        return f"salam from {self.first_name}"
    

class Student(Person):
    def __init__(self, first_name, last_name, father_name, birth_date, birth_place, national_code, hair_color, eye_color, height, weight, std_id):
        super().__init__(first_name, last_name, father_name, birth_date, birth_place, national_code, hair_color, eye_color, height, weight)
        self.std_id = std_id

class Daneshjoo(Student):
    def __init__(self, first_name, last_name, father_name, birth_date, birth_place, national_code, hair_color, eye_color, height, weight, std_id, major):
        super().__init__(first_name, last_name, father_name, birth_date, birth_place, national_code, hair_color, eye_color, height, weight, std_id)
        self.major = major
    
    def say_major(self):
        return f"My major is {self.major}"
    
    def say_hello(self):
        return f"{super().say_hello()}. My major is {self.major}"

class Clerk(Person):
    def __init__(self, first_name, last_name, father_name, birth_date, birth_place, national_code, hair_color, eye_color, height, weight, clerk_id):
        super().__init__(first_name, last_name, father_name, birth_date, birth_place, national_code, hair_color, eye_color, height, weight)
        self.clerk_id = clerk_id

p1 = Person("Ali", "Alavi", "Reza", "1371-07-12", "Rasht", "0123456789", "black", "brown", 180, 75)
d1 = Daneshjoo("Reza", "Ghaemi", "Hassan", "1386-03-23", "Rasht", "1122456789", "gray", "blue", 167, 69, "1298765", "physics")
c1 = Clerk("Ahmad", "Alavi", "Mohammad", "1352-01-02", "Rasht", "0122456887", "white", "brown", 179, 79, "36531")
print(p1.say_hello())
print(d1.say_hello())
print(c1)

# 1 Encapsulation  بسته بندی داده ها
# 2 Inheritence    ارث بری
# 3 Polymorphism   چندریختی
# Object Oriented Programming 