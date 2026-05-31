'''
Write a Python program to check the current position of the file cursor using tell().
'''

file = open("Book.txt",'r')
print("Initial Position : ",file.tell())

file.read(10)
print("Position of reading 10 characters : ",file.tell())

file.close()
