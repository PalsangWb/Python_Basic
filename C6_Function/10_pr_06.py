# WAP to remove a given word from a string and strip it at the same time.
def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "  Hi I am new to code.     "
n = remove_and_split(this, "Palsang")
print(n)