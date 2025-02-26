# By using static method
class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"The salary for working in {self.company} is {self.salary}. \n{signature}")

    @staticmethod #Doesn't need self parameter using this method
    def greet():
        print("Hello World")

    @staticmethod 
    def time():
        print("The time is 6pm now.")

palsang = Employee()
palsang.salary = "100k"
palsang.getSalary("Thanks!")  # Employee.getSalary(palsang)
palsang.greet()
palsang.time()


