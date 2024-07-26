'''
Write a python function to print first n lines of the following pattern:
***
**
* for n = 3
'''
def print_pattern():
    for i in range(n, 0, -1):
        print('*' * i)

n = int(input("Enter the number: "))
print_pattern()

# Another way of doing this is

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)
