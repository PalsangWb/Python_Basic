#WAP to find out whether a given post is talking about "News" or not.
post = input("Enter the post is talking about: ")

if "news" in post.lower():
    print("Yes, the post is talking about news.")
else:
    print("No, the post is not talking about news.")