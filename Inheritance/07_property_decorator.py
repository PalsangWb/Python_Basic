class Employee:
    company = "Google"
    salary = 10000
    salaryBonus = 5000
    # totalSalary = 15000

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus
    
    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary = 20000

print(e.salary)
print(e.totalSalary)
