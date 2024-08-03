'''
Write a program to makr copy of text file "this.txt".
'''
with open("Chapter9/Practice_set/this.txt") as f:
    content = f.read()

with open("Chapter9/Practice_set/this_copy.txt", "w") as f:
    f.write(content)