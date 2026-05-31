'''Write a Python program to demonstrate the use of super() in inheritance.'''

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor called")

    def show(self):
        print("Animal name:", self.name)

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print("Dog constructor called")

    def show(self):
        super().show()
        print("Dog breed:", self.breed)

# Creating object of Dog class
d = Dog("Tom", "Labrador")

print()
d.show()