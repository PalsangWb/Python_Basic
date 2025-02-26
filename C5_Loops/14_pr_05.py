# WAP to find the factorial of a given number.
# n! = 1 X 2 X 3 X ......... X n

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num+1):
    factorial = factorial * i

print(f"The factorial of {num} is: {factorial}")
