'''Write a Python program to show method overriding.'''

class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting with key")

v = Vehicle()
c = Car()

v.start()
c.start()
