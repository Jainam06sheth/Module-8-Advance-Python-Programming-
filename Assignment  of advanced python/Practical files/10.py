""" Write a Python program to print custom exceptions."""

# Define a custom exception
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be 18 or above"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Invalid age given: {self.age}"
    
def check_voting_eligibile(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print("You are eligible to vote.")


# Main program
try:
    user_age = int(input("Enter your age: "))
    check_voting_eligibile(user_age)

except InvalidAgeError as e:
    print("Custom Exception Caught:")
    print(e)

except ValueError:
    print("Please enter a correct age accept only positive integers .")
