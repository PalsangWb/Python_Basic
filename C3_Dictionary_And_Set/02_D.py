myDict = {
    "fast": "In a quick manner",
    "switch": "Changing",
    "marks": [1, 2, 4],
    "new": {'messi':'player'},
    1:2
}
#Dictionary Methods
#print(list(myDict.keys())) #Print the keys of the dictionary
#print(myDict.values()) #Print the vlaues of the dictionary
#print(myDict.items()) #Prints the (key, value) for all contents of the dictionary

#Updates the dictionary by adding key-value pairs from updateDict
"""print(myDict)
updateDict = {
    "New": "A something which is kind of new lol"
}
myDict.update(updateDict)
print(myDict)"""

print(myDict.get("fast2")) #Returns none as fast2 is not present in the dictionary
print(myDict["fast2"]) #Returns an error as fast2 is not present in the dictionary

