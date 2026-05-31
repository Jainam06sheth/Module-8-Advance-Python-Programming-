"""
1. Write a Python program to search for a word in a string using re.search().
2. Write a Python program to match a word in a string using re.match().
"""

import re

text = "My favourite language is Python."
word = "Python"

# re.search():

search_res = re.search(word, text)

# re.match():

match_res = re.match(word, text)

print("=== Search Result ===")

if search_res:
    print(f"'{word}' found at index: {search_res.start()}")

else:
    print(f"'{word}' was not found in the text.")

print("\n=== Match Result ===")

if match_res:
    print(f"'{word}' is present at the beginning of the text.")

else:
    print(f"'{word}' is not present at the beginning of the text.")