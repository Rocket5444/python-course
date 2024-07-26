'''
Write a python function to print multiplication table of given number.
'''

def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

n = int(input("Enter the number: "))
table(n)

# n = int(input("Enter number: "))

# for i in range(1, n+1):
#     print("*" * i, end="")
#     print()  # print a newline after each row
    