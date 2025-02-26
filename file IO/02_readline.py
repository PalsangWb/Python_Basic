f = open ('first.txt')
# read first line
data = f.readline()
print(data)
# read second line
data = f.readline()
print(data)
# read third line
data = f.readline()
print(data)
# read fourth line and so on.
data = f.readline()
print(data)
f.close()