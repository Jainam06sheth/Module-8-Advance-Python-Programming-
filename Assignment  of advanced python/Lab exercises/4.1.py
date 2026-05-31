'''Write a Python program to read the contents of a file and print them on the console.'''

try:
    with open('friend.txt', "r") as file:
        content = file.read()
        print("--- Content of the file  ---")
        print(content)
        print("-----------------------")

except FileNotFoundError:
    print(f"Your, {'friend.txt'} is not there '!")
    