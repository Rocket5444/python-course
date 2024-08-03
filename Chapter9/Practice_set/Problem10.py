'''
Write a program to wipe out the content of a file using python
'''
with open("Chapter9/Practice_set/log.txt", "w") as f:
    f.write("")
print("File content has been wiped out")