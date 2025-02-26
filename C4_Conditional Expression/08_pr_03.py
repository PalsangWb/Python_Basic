# A spam comment is defined as a text combining following keywords.
"""" "make a lot of money", "do this", "do that", "You cannot do that"
""" #WAP to delete these spams.
text = input("Enter the text: ")

if("make a lot of money" in text):
    spam = True
elif("do this" in text):
    spam = True
elif("do that" in text):
    spam = True
elif("you cannot do that" in text):
    spam = True
else:
    spam = False   

if (spam):
    print("This text is spam")

else:
    print('This text is not a spam')






