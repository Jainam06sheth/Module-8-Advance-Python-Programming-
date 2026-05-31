'''
Write a Python program to create a file and print the string into the file. 
'''
file  = open("Book.txt",'r')
print("\n--> Content of File: ")
print(file.read())
file.close()
