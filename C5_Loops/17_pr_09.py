user = int(input("Enter the number you want to print reverse multiplication of: "))

print(f"The multiplication table of {user} in reversed is given below.")

for i in range(11, 1):
    print(f"{user * i} = {user} X {i}")