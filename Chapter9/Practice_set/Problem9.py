'''
Write a program to find out whether a file is identical & mathes the content of the 
another file.
'''
with open("Chapter9/Practice_set/file1.txt") as f:
    content1 = f.read()

with open("Chapter9/Practice_set/file2.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical")

else:
    print("No these files are not identical")
    