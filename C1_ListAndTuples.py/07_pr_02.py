# WAP to accept marks of 6 students and display them in a sorted manner.))
s1 = int(input("Enter marks of a student 1: "))
s2 = int(input("Enter marks of a student 2: "))
s3 = int(input("Enter marks of a student 3: "))
s4 = int(input("Enter marks of a student 4: "))
s5 = int(input("Enter marks of a student 5: "))
s6 = int(input("Enter marks of a student 6: "))

myList = [s1, s2, s3, s4, s5, s6]
myList.sort()
print(myList)