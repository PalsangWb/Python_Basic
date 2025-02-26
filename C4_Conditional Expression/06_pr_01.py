#WAP to find the greatest of four numbers entered by the user.
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))
num4 = int(input("Enter the number4: "))

if (num1>num2):
    f1 = num1
else:
    f1 = num2
     
if (num3>num4):
    f2 = num3
else:
    f2 = num4

if (f1>f2):
    print(f"The greatest number is: {f1}")    
else:
    print(f"The greatest number is: {f2}")    

