'''
Write a program to find out the line number where the word python is present from problem 6
'''

lineno = 1
with open("Chapter9/Practice_set/log.txt") as f:
    lines = f.readlines()

for line in lines:
    if("python" in line):
        print(f"Yes python is present. Line no:{lineno}")
    lineno += 1

else:
    print("No python is not present")