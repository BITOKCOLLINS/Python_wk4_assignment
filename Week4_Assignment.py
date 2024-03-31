#1.Create a Python class named Person.
#2.The Person class should have the following attributes:
# >name: representing the person's name.
# >age: representing the person's age.
# >gender: representing the person's gender.
# 1.Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
# 2.Create an instance of the Person class and call the introduce method to display the person's information.


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

#Usage
person1 = Person("Bitok", 24, "Male")
person1.introduce()  

person2 = Person("Nelly", 21, "Female")
person2.introduce()
