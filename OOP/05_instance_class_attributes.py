class Employee:
    company = "Google"  #Specific to each class
    salary = "10k"

palsang = Employee()  #Object instantiation
nischay = Employee() 

# Creating instance attribute salary for both the oblects
# First try to associate with object and then class.
# palsang.salary = "30k"  #Adding instance attribute
# nischay.salary = "40k"
palsang.salary = "5k"

print(palsang.company)
print(nischay.company)

Employee.company = "Youtube"  #Changing the class attribute
print(palsang.company)
print(nischay.company)

print(palsang.salary)
print(nischay.salary)

#Below line throws an error as address is not present in instance/class
# print(palsang.address)