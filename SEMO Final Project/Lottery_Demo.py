letter = '''Dear <|NAME|>,
Greeting to learn write a letter.
You are selected!
Date: <|DATE|>
''' 
name = input("Enter your name: ")
date = input("Enter date: ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)