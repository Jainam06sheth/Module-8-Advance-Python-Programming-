try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))

    result = num1 / num2
    print("Result =", result)

    # Save result to calculator.txt
    with open("calculator.txt", "a") as file:
        file.write(f"{num1} / {num2} = {result}\n")

    print("Result saved in calculator.txt")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numeric input.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("Program execution completed.")