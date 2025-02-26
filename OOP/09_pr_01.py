# Create a class programmer for storing information of few programmers working at microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the programmer is {self.name} and the product is {self.product}.")

palsang = Programmer("Palsang", "Forte Series")
sunil = Programmer("Sunil", "SpaceX")

palsang.getInfo()
sunil.getInfo()

