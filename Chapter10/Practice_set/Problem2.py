'''
Write a class "calculator" capable of finding square, cube and root of a number.
'''
class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square is {self.num*self.num}")

    def cube(self):
        print(f"rhe cube of the number is {self.num*self.num*self.num}")

    def squareroot(self):
        print(f"The square root is {self.num**1/2}")

print("1] Find square of the number: ")
print("2] Find cube of the number: ")
print("3] Find square root of the number: ")
b = int(input("Enter the choice: "))
n = int(input("Enter the number: "))
a = calculator(n)
if(b == 1):
    a.square()
elif(b == 2):
    a.cube()
elif(b == 3):
    a.squareroot()
else:
    print("You have enterd the wrong choice: ")
