#WAP to find sum of first n natural number using the while loop.
sum = 0

for i in range(1, 6):
    sum = i + sum
    print(f"The sum of first natural numbers upto {i} are: {sum}")