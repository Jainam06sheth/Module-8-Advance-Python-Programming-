''' Write a Python program to search for a word in a string using re.search().'''

import re

text = "Python is a powerful programming language."
word = "powerful"

result = re.search(word, text)

if result:
    print("Word found!")
else:
    print("Word not found!")