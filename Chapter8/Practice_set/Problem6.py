'''
write a python function which conerts inches into cms
'''

def convert():
    a = int(input("Enter the value in the inches: "))
    ans = (a * 2.54)
    print("The value in cm is: ", ans)

convert()