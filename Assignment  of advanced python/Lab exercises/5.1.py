'''Write a Python program to create a class and access its properties using an object.'''

def calculator():
    print('==-- Simple Calculator --==')
    status = True
    while status:
        
        try:
            num1 = float(input("Enter the 1st number : "))
            op = input("Enter the operator(+,-,*,/) : ")
            num2 = float(input("Enter the 2nd number : "))
            
            if op == '+' :
                result = num1+ num2
            
            elif op == '-':
                result = num1 - num2
            
            elif op == '*':
                result = num1 * num2   
            
            elif op == '/':
                result = num1 / num2
                    
            else :
                print("Invalid Operator!Please enter (+,-,*,/).")
                continue

            print(f"Result:{result:f}")
            break        
        
        except ValueError:
            print("Please enter the correct value.")
            
        except ZeroDivisionError:
            print("Divide by 0 is not valid.")
            
        except Exception as e :
            print(f"Unexpected error : {e}")        
            
calculator()