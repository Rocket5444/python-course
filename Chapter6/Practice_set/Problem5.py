# Write a program which finds out whether a given name is present in list or not.
l = ["Harry", "Kunal", "Shubham", "Anushka"]

name = input("Enter your name: ")

if(name in l):
    print("Your name is present in the list")

else:
    print("Your name is not in the list")