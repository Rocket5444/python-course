# If you have more than a one conditions then use elif condition

a = int(input("Enter your age: "))

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid age")

else:
    print("you are below the age of consent")

print("End of the program")