# Create a class with a class attribute a; create an object from it and set a directly using object. a = 0
# Does this change the class attribute?

class Sample:
    a = "Palsang"

obj = Sample()
obj.a = "Nischay"

print(Sample.a)
print(obj.a)
