'''Write a Python program to write multiple strings into a file.'''

lines_to_write = [
    'Hello! My name is Jainam!\n',
    'When you came India then you gave me a party\n',
    'We are the best friends\n',
]

with open('friend.txt','w') as file:
    file.writelines(lines_to_write)
    print(f"The {'friend.txt'} is upgraded!")