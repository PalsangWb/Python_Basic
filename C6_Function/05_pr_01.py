# WAP using function to find the greatest of three number.

def maximum(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    else:
        if (num2 > num3):
            return num2
        else:
            return num3

G = maximum(100, 200, 50000)
print(f"The greatest number among the 3 numbers are: {G}")


        


        
   