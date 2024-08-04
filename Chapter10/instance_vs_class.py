''''
An attribute that belong to the Instance(object). Assuming the class from the previous

Note: Instance attrinutes, take preferances over class attributes during assignment &
retrival.
'''

class Employee:
    language = "Python" # This is class attribute 
    salary = 1200000

harry = Employee()
harry.language = "JavaScript" # This is a instance attribute
print(harry.language, harry.salary)