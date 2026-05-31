'''Write a Python program to show single inheritance. '''

# Parent class:
class Animal:
    def eat(self):
        print("This animal eats food.")

# Child class inheriting from Animal:
class Dog(Animal):
    def bark(self):
        print("Dog barks.")

# Creating object of child class:
d = Dog()

# Calling method of parent class:
d.eat()

# Calling method of child class:
d.bark()