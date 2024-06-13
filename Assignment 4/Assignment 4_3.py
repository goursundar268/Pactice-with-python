# Write a  program to demonstrate Object and Class in  Python.

class Employee:
    def __init__(self,name,post):
        self.name=name
        self.post=post

    def salary(self,salary):
        self.salary=salary
        print(f"{self.name} is posted on {self.post}")
        print(f"his Salary is{self.salary}")

A1=Employee("Ram","Manager")
A1.salary(50000)