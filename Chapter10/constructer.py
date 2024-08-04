class Employee:
    language = "Python"
    salary = 12000000

    def __init__(self, name, salary, language): # It is dunder method which is automatically called it start with the doble underscore
        print("I am creating an object")
        self.name = name
        self.salary = salary
        self.language = language

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee("Kunal", 1300000, "JavaScript")
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)