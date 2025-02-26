def percentage(marks):
    p = ((marks1[0] + marks1[1] + marks1[2] + marks1[3])/400) * 100
    return p

marks1 = [50, 60, 70 ,80]
percentage1 = percentage(marks1)

marks2 = [80, 60, 70 ,50]
percentage2 = percentage(marks2)

print(percentage1, percentage2)

# A fucntion can be reused by the programmer in a given program any number of time.