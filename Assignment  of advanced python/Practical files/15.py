'''Write a Python program to show multiple inheritance'''

class Father:
    def _father(self):
        print("Father: Cooking skills")

class Mother:
    def _mother(self):
        print("Mother: Painting skills")

class Child(Father, Mother):
    def _child(self):
        print("Child: Sports skills")

# Creating object of Child class
c = Child()

# Accessing methods from both parent classes
c._father()
c._mother()

# Accessing child class method
c._child()