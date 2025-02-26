class Person:
    country = "Nepal"

    def __init__(self):
        print("Initializing Person...\n")

    def takeBreak(self):
        print("I am taking some work.")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")
        

    def getSalary(self):
        super().takeBreak()
        print(f"Your salary is {self.salary}")

    def takeBreak(self):
        print(f"I am thinking to take some break so I will tour 'Manang' or 'Mustang'")

class Programmer(Employee):
    company = "Maruti"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer...\n")
        

    def getSalary(self):
        print("No salary to beginner.")

    def takeBreak(self):
        super().takeBreak()
        print("I am going in 2025.")

a = Person()
#a.takeBreak()
#print(a.company) #Throws an error because parent class has no company
#print(a.country)

b = Employee()
#b.takeBreak()
#print(b.country) #Doesn't throws an error becuase parent class has country class
#print(b.company)

c = Programmer()
#c.getSalary()
#c.takeBreak()




