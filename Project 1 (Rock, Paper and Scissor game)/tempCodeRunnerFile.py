import random

def game(comp, you):
    if comp == you:
        return None
    elif comp == "r":
        if you == "p":
            return True
        elif you == "s":
            return False
    elif comp == "p":
        if you == "s":
            return True   
        elif you == "r":
            return False 
    elif comp == "s":
        if you == "r":
            return True
        elif you == "p":
            return False

print("Computer's turn: Rock(r), Paper(p) or Scissor(s).")
RandomNumber = random.randint(1, 3)
if RandomNumber == 1:
    comp = "r"
elif RandomNumber == 2:
    comp = "p"
elif RandomNumber == 3:
    comp = "s"

you = input("Enter your options: Rock(r), Paper(p) or Scissor(s):")

result = game(comp, you)
print(f"Computer choice: {comp}")
print(f"Your choice: {you}")

if result == None:
    print("The game is a tie.")
elif result:
    print("You win.")
else:
    print("You lose.")
