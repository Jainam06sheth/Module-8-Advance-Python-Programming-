'''Write a Python program to open a file in write mode, write some text, and then close it'''

with open("friend.txt", "w") as file:
    file.write("Hey! My name is Jainam. Fenil is my bestfriend. \n")
    file.write("I want to meet you in India. He is not my bestfriend but my brother like best friend.")
    
print("The file is written...")