# Multiple Inheritance 

class Employee:
    company = "Google"
    Position = 1

class Freelancer:
    company = "Python Networking"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Palsang"

p = Programmer()
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.company) # Why google is printing first because Programmer(Employee, Freelancer)