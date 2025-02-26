# WAP to create a dictionary of Nepali Words with vlaues as their english Translation. 
# Provide user with an option to look it up.

NepDict = {
    "jado": "Cold",
    "garmi": "Hot",
    "bag": ["pencil", "pen", "Bottle"]
}
print(f"Options are: {NepDict.keys()}")
user = input("Enter the Nepali word: ")
print(f"The meaning of your word in English is: {NepDict[user]}")

