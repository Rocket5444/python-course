'''
Write a program using functions to find greatest of three numbers.
'''

def greatest():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    c = int(input("Enter the third number:"))

    if(a>b and a>c):
        print("The greatest number is: ", a)

    elif(b>a and b>c):
        print("The greatest number is: ", b)

    else:
        print("The greatest number is: ", c)
        
greatest()