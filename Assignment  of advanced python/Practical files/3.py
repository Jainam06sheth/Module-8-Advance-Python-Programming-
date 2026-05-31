'''
Write a Python program to create a file and write a string into it.
'''

file = open("Book.txt",'w')  
file.write("Hello, Python is invented by Guido van Rossum.")
file.close()

print("The data is written successfully.")
