'''
Write a python program to rename a file to "renamed_by_python.txt".
'''

with open("Chapter9/Practice_set/old.txt") as f:
    content = f.read()

with open("Chapter9/Practice_set/renamed_by_python.txt", "w") as f:
    f.write(content)