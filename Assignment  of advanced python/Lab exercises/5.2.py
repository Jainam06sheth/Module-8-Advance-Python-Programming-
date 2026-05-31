'''Write a Python program to demonstrate handling multiple exceptions.'''

def process_data():
    
    try:
        num = int(input("Enter the number: "))
        divider = int(input("Enter the number to divide: "))
        
        result = num / divider
        print(f"Result: {result:}")
        
        my_list = [20, 30, 40]
        index = int(input("List index (0-2): "))
        print(f"List element: {my_list[index]}")

    except ValueError:
        print("Please enter the number only.")
        
    except ZeroDivisionError:
        print("Divide by zero is not possible!")
        
    except IndexError:
        print("Error: List is not long, index is  done!")
        
    except Exception as e:
        print(f"Unexpected error : {e}")
        
    finally:
        print("\nProcess is over..")

process_data()