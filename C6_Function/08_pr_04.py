# Write a recursive function to calculate the sum of first n natural numbers.
"""
n! = (n-1)! * n
sum(n) = sum(n-1) + n
"""
def sum_rec(n):
    if n==1 or n==0:
        return 1
    return sum_rec(n-1) + n

sum = sum_rec(5)
print(f"Sum of natural numbers using recursive function is: {sum}")