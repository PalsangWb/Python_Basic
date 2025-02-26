#An empty set can be created using below syntax:
b = set()
print(type(b))

#Adding values to an empty set
b.add(3)
b.add(3) #Adding a value repeatedly does not change a set
b.add(3)
b.add(3)
b.add(3)
b.add(4)
#b.add([1, 2, 4]) #Cannot add list inside
b.add((1, 2, 3, 4, 4)) #Can add tuple
#b.add({4:5}) #Cannot add dictionary

print(b)

#Lengthe of the set
print(len(b)) #Prints the length of this set

#Removal of an item
b.remove(3) #Removes 3 from set but cannot remove which is not there
#b.remove(12) #Throws an error while trying to remove 12( which is not present in the set)
print(b)

print(b.pop()) #Removes an arbitary element from the set and returns the element removed
print(b)