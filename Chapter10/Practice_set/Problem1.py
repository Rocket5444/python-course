'''
Create a class "Programmer" for storing information of few programmers
wroking at microsoft.
'''

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("harry", 120000, 413708)
print(p.name, p.company, p.pin, p.salary)