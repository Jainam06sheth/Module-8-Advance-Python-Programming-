'''Write a Python program to show hierarchical inheritance. '''

# Parent Class
class Animal:
    def eat(self):
        print("This animal is eating food.")

# Child 1
class Dog(Animal):
    def bark(self):
        print("Dog says: Woof! Woof!")

# Child 2
class Cat(Animal):
    def meow(self):
        print("Cat says: Meow! Meow!")


d = Dog()
c = Cat()

d.eat()
d.bark()

print("-" * 20)

c.eat()
c.meow()