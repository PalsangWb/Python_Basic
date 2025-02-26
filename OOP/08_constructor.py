class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created.")

    def getDetails(self):
        print(f"The name of the employee is {self.name}.")
        print(f"The name of the employee is {self.salary}.")
        print(f"The subunit of the employee is {self.subunit}.")

    def getSalary(self, signature):
        print(f"The salary for working in {self.company} is {self.salary}. \n{signature}")

    @staticmethod #Doesn't need self parameter using this method
    def greet():
        print("Hello World")

    @staticmethod 
    def time():
        print("The time is 6pm now.")

palsang = Employee("Palsang", 100000, "YouTube")
# palsang = Employee() --> This throws an error(missing 3 required arguments.)
palsang.getDetails()



