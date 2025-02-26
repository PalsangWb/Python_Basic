class Employee:
    company = "Google \n"

    def showDetails(self):
        print("This is an employee.")

class Programmer(Employee):
    language = "Python"
    company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}.")

    def showDetails(self):
        print("This is an overriding.")



e = Employee()
e.showDetails()
print(e.company)
p = Programmer()
p.showDetails()
print(p.company)


        