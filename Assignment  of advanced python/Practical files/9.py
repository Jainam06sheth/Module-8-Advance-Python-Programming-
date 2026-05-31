'''
Python Program to Handle File Exceptions and Use finally Block
'''
file = None

try:
    file = open("calculator.txt", "r")
    content = file.read()
    print("File Content:")
    print(content)

except FileNotFoundError:
    print("Error: File not found.")

except IOError:
    print("Error: Unable to read the file.")

finally:
    if file is not None:
        file.close()
        print("File closed successfully.")