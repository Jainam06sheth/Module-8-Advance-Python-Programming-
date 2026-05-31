'''
Write Python programs to demonstrate method overloading and method overriding.
'''

# method overriding  
print("---Method Overriding---")
class Animal:
    def speak(self):
        print("Animal sound karta hai.")

class Dog(Animal):
    def speak(self):
        print("Dog sounds Bow Wow!")

class Cat(Animal):
    def speak(self):
        print("Cat sounds Mew Mew.")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

# overloading
print("\n---Method Overloading---")
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()

print(f"Sum of 2 numbers: {calc.add(6, 12)}")
print(f"Sum of 3 numbers: {calc.add(6, 12, 18)}")