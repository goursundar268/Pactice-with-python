# Write a program to demonstrate Inheritance in python.

class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"{self.name} is able of make sound")
class Dog(Animal):
    def __init__(self,name,bread):
        self.name=name
        self.bread=bread
dog=Dog("Buddy","Labradar")
dog.speak()