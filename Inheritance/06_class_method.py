class Employee:
    company = "Google"
    salary = 100
    location = "New York"

    # def changeSalary(self, sal):  # To change the salary of the class.
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal   # This will change the salary of the instance of the class.

e = Employee()
print(e.salary)
e.changeSalary(500)

print(Employee.salary)
print(e.salary)
