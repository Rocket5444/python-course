class Employee:
    language = "Python"
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

harry = Employee()
harry.language = "JavaScript"
harry.getInfo()  # Output: The language is JavaScript. The salary is 120000
# Employee.grtInfo(harry) You can write the above statement like this