#WAP to calulate the grade of the student from his marks from the following scheme.
"""90-100 = Ex
   90-80 = A
   80-70 = B
   70-60 = C
   60-50 = D
   40-30 = Fail"""
marks = int(input("Enter your marks: "))

if marks>=90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"  
else:
    grade = "Fail"  

print(f"Your grade is:{grade}")
