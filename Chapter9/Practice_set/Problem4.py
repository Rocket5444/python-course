'''
A file contains a word "Donkey" multiple times. You need to write a program which 
replace this word with #### by updating the same file.
'''
word = "Donkey"

with open("Chapter9/Practice_set/file .txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "#####")

with open("Chapter9/Practice_set/file .txt", "w") as f:
    f.write(contentNew)