'''Write a Python program to match a word in a string using re.match().'''

import re 

text = "Python is a powerful programming language."
word = "Python"

result = re.match(word, text)

if result:
    print("Match found!")
else:
    print("No match found!")