#WAP to print multiplication table of a given number using for loop.
user = int(input("Enter the number you want multiplication of: "))

print(f"The multiplication table of {user} is given below.")

for i in range(1, 11):
    print(f"{user} X {i} = {user * i}")