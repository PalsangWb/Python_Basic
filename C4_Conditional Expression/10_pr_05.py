#WAP to find whether a given name is present in  a list or not.
friendNames = ["Sunil", "Rabin", "Nischay", "Yubin", "Prashant", "Shiva"]
name = input("Enter your name please: ")

if (name in friendNames):
    print("The given name is present.")
else:
    print("The name is not present.")