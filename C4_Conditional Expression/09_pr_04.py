#WAP to find whether a given user name contains less than 10 letter or not.
userName = input("Enter your name: ")
if len(userName) < 10:
    print("The name contians less than 10 letters.")
else:
    print("The name contains more than 10 letters.")