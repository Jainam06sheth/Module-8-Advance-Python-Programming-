'''Write a Python program to show multilevel inheritance. '''

class Animal:
    def eat(self):
        print("Animal eats food.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps.")

p = Puppy()

p.eat()    # From Animal class
p.bark()   # From Dog class
p.weep()   # From Puppy class