'''
A function is a group of statement performing a specific task.
    When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what!
    A function can be reused by the programmer in given program any number of
'''
# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))

# average = (a + b + c)/3
# print(average)

# Function Defination
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c)/3
    print(average)

avg() # Function call
print("Thank you!")

'''
There are two types of functions in the pyhton.
1] Builtin Function
2] User Defined Function
'''
