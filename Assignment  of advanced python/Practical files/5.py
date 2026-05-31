'''
Write a Python program to read a file and print the data on the console.
'''

file = open("Book.txt",'r')
data = file.read()
print("--> Read the file : ")
print(data)
file.close()