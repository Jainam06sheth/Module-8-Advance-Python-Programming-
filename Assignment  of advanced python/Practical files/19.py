'''Write a Python program to show method overloading. 
==> Python doesn't supports method overloading...
'''

class Student:

    def show(self, name=None, age=None):
        if name is not None and age is not None:
            print("Name:", name, "Age:", age)

        elif name is not None:
            print("Name:", name)

        else:
            print("No data")


# Object create
s = Student()

s.show("Amit")
s.show("Amit", 20)
s.show()