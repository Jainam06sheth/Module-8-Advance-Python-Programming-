''' Write a Python program to show hybrid inheritance.'''

class Animal:
    def eat(self):
        print("Animal eats food.")

# First child class (Hierarchical inheritance)
class Mammal(Animal):
    def walk(self):
        print("Mammal walks.")

# Second child class (another branch)
class Bird(Animal):
    def fly(self):
        print("Bird flies.")

# Hybrid class (Multiple + Hierarchical inheritance combined)
class Bat(Mammal, Bird):
    def special_feature(self):
        print("Bat can walk and fly.")

# Creating object of Bat class
b = Bat()

# Accessing methods from all parent classes
b.eat()            # from Animal
b.walk()           # from Mammal
b.fly()            # from Bird
b.special_feature() # from Bat