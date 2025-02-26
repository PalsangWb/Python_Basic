"""
Create a class Employee and add salary and increment properties to it. Write a method SalaryAfterIncrement method
with a @property decorator with a setter which changes the value of increment based on the salary.
"""
# salaryAfterIncrement = Salary * Increment

class Employee:
    def __init__(self, salary = 10000, increment = 1.5):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salaryAfterIncrement):
        self.increment = salaryAfterIncrement / self.salary

e = Employee()

print(e.salaryAfterIncrement)
print(e.increment)

e.salaryAfterIncrement = 20000
print(e.salaryAfterIncrement)
print(e.increment)