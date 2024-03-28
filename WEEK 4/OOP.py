class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello! My name is {self.name}. I am {self.age} years old and identify as {self.gender}.")

person_instance = Person(name="Alice", age=30, gender="female")

person_instance.introduce()
