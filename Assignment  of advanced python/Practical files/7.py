'''
Write a Python program to handle exceptions in a calculator. 
''' 
status = True
def calculator():
    print("==-->Calculator : ")
    
    while status:
    
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            op = input("Enter operator (+, -, *, /): ")

            if op == '+':
                print("Addition : ", num1 + num2)
            elif op == '-':
                print("Subtraction : ", num1 - num2)
            elif op == '*':
                print("Multiplication : ", num1 * num2)
            elif op == '/':
                print("Divission : ", num1 / num2)
            else:
                print("Invalid operator")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Please enter valid numbers.")