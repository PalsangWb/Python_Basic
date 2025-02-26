# WAP to find out whether a student is pass or fail, if the total is 40% and at least 35% in each subject to pass.
#Assume 3 subjects and take marks as an input from the user.
sub1 = int(input("Enter the first subject marks: "))
sub2 = int(input("Enter the second subject marks: "))
sub3 = int(input("Enter the third subject marks: "))

if (sub1<35 or sub2<35 or sub3<35):
    print("Sorry!You have less than 35 percentage in one of the subject.")

elif(sub1+sub2+sub3)/3 < 40:
    print("Your total is less than 40 percentage. Sorry! You are fail.")    

else:
    print("You are pass.")    


