f = open("Chapter9/file.txt")

# Readlines function in pyhton for file handling.
# lines = f.readlines()

# print(lines, type(lines))


# Readline function in pyhton for file handling.

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# For reading all the lines in the file
# This will print all the until the file comes to an end.

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()


f.close()