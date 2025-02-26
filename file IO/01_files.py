# Use open function to read the content of a file:
#a = open("first.txt", "r")
a = open("first.txt", "r") # by defaultvthe mode is r
#data = a.read()
data = a.read(5) # reads first 5 characters from the file
print(data)
a.close()
