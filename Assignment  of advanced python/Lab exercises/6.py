'''
Write a Python program to create a class and access its properties using an object.
'''

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print(f"Student name : {self.name}")
        print(f"Student age : {self.age} years.")
        
s1 = Student("Jainam",21)
print(f"Your name: {s1.name} and age : {s1.age} years")            