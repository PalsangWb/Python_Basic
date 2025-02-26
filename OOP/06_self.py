# By using self you can use both class and instance attributes.
class Employee:
    company = "Google"
    def getSalary(self):
        print(f"The salary for working in {self.company} is {self.salary}.")

    # @staticmethod
    # def greet():
    #     print("Hello World")


palsang = Employee()
palsang.salary = "100k"
palsang.getSalary()  # Employee.getSalary(palsang)
