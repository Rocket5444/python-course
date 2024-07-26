'''
Write a python program using function to convert celsius to Fahernheit.
'''

def convert():
    a = int(input("Enter the temprature in Celsius: "))

    b = ((a * 9/5) + 32)
    print("The temprature in Fahrenheit is:", b)

convert()